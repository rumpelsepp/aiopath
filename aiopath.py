from __future__ import annotations

import os
from asyncio import to_thread
from pathlib import Path, PurePosixPath
from typing import (
    Any,
    AsyncGenerator,
    Generator,
    ParamSpec,
    Union,
)

import aiofiles
from aiofiles.base import AiofilesContextManager


P = ParamSpec("P")


class AsyncPath(PurePosixPath):
    def __init__(self, path: Union[str, os.PathLike[str]]) -> None:
        super().__init__()
        self.sync_path = Path(path)

    async def stat(self, *args: P.args, **kwargs: P.kwargs) -> os.stat_result:
        return await to_thread(self.sync_path.stat, *args, **kwargs)

    async def chmod(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.chmod, *args, **kwargs)

    async def exists(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.exists, *args, **kwargs)

    async def expanduser(self, *args: P.args, **kwargs: P.kwargs) -> AsyncPath:
        return AsyncPath(await to_thread(self.sync_path.expanduser, *args, **kwargs))

    async def glob(
        self, *args: P.args, **kwargs: P.kwargs
    ) -> Generator[Path, None, None]:
        return await to_thread(self.sync_path.glob, *args, **kwargs)

    async def group(self, *args: P.args, **kwargs: P.kwargs) -> str:
        return await to_thread(self.sync_path.group, *args, **kwargs)

    async def is_dir(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_dir, *args, **kwargs)

    async def is_file(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_file, *args, **kwargs)

    async def is_mount(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_mount, *args, **kwargs)

    async def is_symlink(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_symlink, *args, **kwargs)

    async def is_socket(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_socket, *args, **kwargs)

    async def is_fifo(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_fifo, *args, **kwargs)

    async def is_block_device(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_block_device, *args, **kwargs)

    async def is_char_device(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.is_char_device, *args, **kwargs)

    async def iterdir(self) -> AsyncGenerator[AsyncPath, None]:
        for name in await to_thread(os.listdir, self):
            yield self.__class__(name)

    async def lchmod(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.lchmod, *args, **kwargs)

    async def lstat(self, *args: P.args, **kwargs: P.kwargs) -> os.stat_result:
        return await to_thread(self.sync_path.lstat, *args, **kwargs)

    async def mkdir(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.mkdir, *args, **kwargs)

    # XXX: Implement this without aiofiles.
    def open(
        *args: P.args, **kwargs: P.kwargs
    ) -> AiofilesContextManager[None, None, Any]:
        return aiofiles.open(*args, **kwargs)  # type: ignore

    async def owner(self, *args: P.args, **kwargs: P.kwargs) -> str:
        return await to_thread(self.sync_path.owner, *args, **kwargs)

    async def read_bytes(self, *args: P.args, **kwargs: P.kwargs) -> bytes:
        return await to_thread(self.sync_path.read_bytes, *args, **kwargs)

    async def read_text(self, *args: P.args, **kwargs: P.kwargs) -> str:
        return await to_thread(self.sync_path.read_text, *args, **kwargs)

    async def readlink(self, *args: P.args, **kwargs: P.kwargs) -> AsyncPath:
        return AsyncPath(await to_thread(self.sync_path.readlink, *args, **kwargs))

    async def rename(self, *args: P.args, **kwargs: P.kwargs) -> AsyncPath:
        return AsyncPath(await to_thread(self.sync_path.rename, *args, **kwargs))

    async def replace(self, *args: P.args, **kwargs: P.kwargs) -> AsyncPath:
        return AsyncPath(await to_thread(self.sync_path.replace, *args, **kwargs))

    async def rglob(
        self, *args: P.args, **kwargs: P.kwargs
    ) -> Generator[Path, None, None]:
        return await to_thread(self.sync_path.rglob, *args, **kwargs)

    async def rmdir(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.rmdir, *args, **kwargs)

    async def samefile(self, *args: P.args, **kwargs: P.kwargs) -> bool:
        return await to_thread(self.sync_path.samefile, *args, **kwargs)

    async def symlink_to(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.symlink_to, *args, **kwargs)

    async def shardlink_to(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.hardlink_to, *args, **kwargs)

    async def touch(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.touch, *args, **kwargs)

    async def unlink(self, *args: P.args, **kwargs: P.kwargs) -> None:
        return await to_thread(self.sync_path.unlink, *args, **kwargs)

    async def write_bytes(self, *args: P.args, **kwargs: P.kwargs) -> int:
        return await to_thread(self.sync_path.write_bytes, *args, **kwargs)

    async def write_text(self, *args: P.args, **kwargs: P.kwargs) -> int:
        return await to_thread(self.sync_path.write_text, *args, **kwargs)
