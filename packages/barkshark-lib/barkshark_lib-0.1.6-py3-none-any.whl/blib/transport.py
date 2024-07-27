from __future__ import annotations

import asyncio
import sys

from collections.abc import Callable, Generator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, AnyStr, IO, TypeVar

from .misc import catch_errors, convert_to_bytes

if TYPE_CHECKING:
	try:
		from typing import Self

	except ImportError:
		from typing_extensions import Self


T = TypeVar("T")
STDIO: AsyncTransport | None = None


async def aprint(
				*text: str,
				separator: str = " ",
				newline: bool = True,
				flush: bool = True) -> None:
	"""
		Print some text to stdout.

		:param text: Objects to print out. They will be converted to strings.
		:param separator: Character(s) to use when separating multiple items
		:param newline: Add a newline character to the end of the string
		:param flush: Dump any currently queued data to be sent to stdout
	"""

	stdio = await AsyncTransport.from_stdio()
	data = separator.join(str(item) for item in text).encode(stdio.encoding)

	if newline:
		data += b"\n"

	await stdio.write(data, flush)


async def aprompt(
				prompt: str,
				deserializer: Callable[[str], T] = str, # type: ignore[assignment]
				choices: list[T] | None = None,
				default: T | None = None) -> T:
	"""
		Ask the user for a response to a question via stdout. Returns a :class:`str` by default.

		:param prompt: Text to display to the user
		:param deserializer: Function that converts the response to the correct type
		:param choices: Only valid replies if set
		:param default: Value to return if a user doesn't provide an answer
	"""

	if choices is not None and default is not None and default not in choices:
		raise ValueError("Default value not in available choices")

	while True:
		trans = await AsyncTransport.from_stdio(timeout = -1)
		line2 = f"[{default}]: " if default is not None else ": "

		if choices is not None:
			str_choices = ", ".join(str(c) for c in choices)
			await trans.write(f"{prompt} [{str_choices}]\n{line2}")

		else:
			await trans.write(f"{prompt}\n{line2}")

		if (raw_value := (await trans.readline()).decode("utf-8").strip()) == "":
			if default is None:
				await aprint("No response")
				continue

			return default

		value = deserializer(raw_value)

		if choices is not None and value not in choices:
			await aprint("Not a valid choice")
			continue

		return value


class AsyncTransport:
	"Transport class for ``StreamReader`` and ``StreamWriter`` objects"


	def __init__(self,
				reader: asyncio.StreamReader,
				writer: asyncio.StreamWriter,
				timeout: int = 60,
				encoding: str = "utf-8") -> None:
		"""
			Create a new async transport

			:param reader: Reader object
			:param writer: Writer object
			:param timeout: Time to wait for read methods before giving up
			:param encoding: Text encoding to use when converting text to bytes
		"""

		self.reader: asyncio.StreamReader = reader
		"Reader object"

		self.writer: asyncio.StreamWriter = writer
		"Writer object"

		self.encoding: str = encoding
		"Text encoding to use when converting text into bytes"

		self.timeout: int = timeout
		"Time to wait for read methods before giving up"


	async def __aenter__(self) -> Self:
		return self


	async def __aexit__(self, *_: Any) -> None:
		await self.close()


	@classmethod
	async def from_fp(cls: type[Self],
					r_fp: IO[AnyStr],
					w_fp: IO[AnyStr] | None = None,
					timeout: int = 60,
					encoding: str = "utf-8") -> Self:

		loop = asyncio.get_running_loop()
		reader = asyncio.StreamReader()
		protocol = asyncio.StreamReaderProtocol(reader)

		await loop.connect_read_pipe(lambda: protocol, r_fp)
		trans, proto = await loop.connect_write_pipe(asyncio.streams.FlowControlMixin, w_fp or r_fp)

		return cls(
			reader,
			asyncio.StreamWriter(trans, proto, reader, loop),
			timeout,
			encoding
		)


	@classmethod
	async def from_stdio(cls: type[Self], timeout: int = 60, encoding: str = "utf-8") -> Self:
		global STDIO

		if STDIO is None:
			STDIO = await cls.from_fp(sys.stdin, sys.stdout, timeout, encoding)

		return STDIO # type: ignore[return-value]


	@classmethod
	async def new_client(
					cls: type[Self],
					*args: Any,
					timeout: int = 5,
					unix: bool = False,
					**kwargs: Any) -> Self:

		reader: asyncio.StreamReader
		writer: asyncio.StreamWriter

		if unix:
			reader, writer = await asyncio.open_unix_connection(*args, **kwargs)

		else:
			reader, writer = await asyncio.open_connection(*args, **kwargs)

		return cls(reader, writer, timeout = timeout)


	@property
	def eof(self) -> bool:
		"Checks if the reader has reached the end of the stream"

		return self.reader.at_eof()


	@property
	def local_address(self) -> str:
		"Get the address of the local socket"

		return self.writer.get_extra_info('sockname')[0] # type: ignore[no-any-return]


	@property
	def local_port(self) -> int:
		"Get the port of the local socket"

		return self.writer.get_extra_info('sockname')[1] # type: ignore[no-any-return]


	@property
	def remote_address(self) -> str:
		"Get the address of the remote socket"

		return self.writer.get_extra_info('peername')[0] # type: ignore[no-any-return]


	@property
	def remote_port(self) -> int:
		"Get the port of the remote socket"

		return self.writer.get_extra_info('peername')[1] # type: ignore[no-any-return]


	async def close(self) -> None:
		"Close the writer stream"

		if self.writer.can_write_eof():
			self.writer.write_eof()

		self.writer.close()

		with catch_errors(True):
			await self.writer.wait_closed()


	async def read(self, length: int = -1) -> bytes:
		"""
			Read a chunk of data

			:param length: Amount of data in bytes to read
		"""

		return await asyncio.wait_for(self.reader.read(length), self.timeout)


	async def readline(self, limit: int = 65536) -> bytes:
		"""
			Read until a line ending ('\\\\r' or '\\\\n') is encountered

			:param limit: Maximum number of bytes to return
		"""

		with self._set_limit(limit):
			return await asyncio.wait_for(self.reader.readline(), self.timeout)


	async def readuntil(self, separator: bytes | str, limit: int = 65536) -> bytes:
		"""
			Read upto the separator

			:param separator: Text or bytes to stop at
			:param limit: Maximum number of bytes to return
		"""

		if isinstance(separator, str):
			separator = separator.encode(self.encoding)

		with self._set_limit(limit):
			return await asyncio.wait_for(self.reader.readuntil(separator), self.timeout)


	async def write(self, data: Any, flush: bool = True) -> None:
		"""
			Send data

			:param data: Data to be sent
			:param flush: Send all queued data now if ``True``
		"""

		data = convert_to_bytes(data, self.encoding)
		self.writer.write(data)

		if flush:
			await self.writer.drain()


	@contextmanager
	def _set_limit(self, limit: int = 65536) -> Generator[None, None, None]:
		orig_limit = self.reader._limit # type: ignore[attr-defined]
		self.reader._limit = limit # type: ignore[attr-defined]

		try:
			yield

		finally:
			self.reader._limit = orig_limit # type: ignore[attr-defined]
