#!/usr/bin/env python3

"""Sets up a RAM-disk"""

import os

from config import config


class RAMBlockDev:
    """
    Taken from https://docs.micropython.org/en/latest/reference/filesystem.html
    """

    def __init__(self, block_size: int, num_blocks: int) -> None:
        self.block_size = block_size
        self.data = bytearray(block_size * num_blocks)

    def readblocks(self, block_num: int, buf: bytearray, offset: int = 0) -> None:
        """Read @block_num blocks into @buf"""
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            buf[i] = self.data[addr + i]

    def writeblocks(self, block_num: int, buf: bytearray, offset: int = None) -> None:
        """Write @block_num blocks into @buf"""
        if offset is None:
            # do erase, then write
            for i in range(len(buf) // self.block_size):
                self.ioctl(6, block_num + i)
            offset = 0
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            self.data[addr + i] = buf[i]

    def ioctl(self, op: int, arg: object) -> int:
        """ioctl"""
        if op == 4:  # block count
            return len(self.data) // self.block_size
        if op == 5:  # block size
            return self.block_size
        if op == 6:  # block erase
            return 0


def setup_ramfs(mountpoint, block_size, num_blocks):
    """Setup a RAM-FS we can use for storing files without wearing off the
    flash memory
    """
    if mountpoint.split("/")[-1] in os.listdir():
        print(f"{mountpoint} exists - exit")
        return
    if sys.platform == "linux":
        os.mkdir(os.path.join(os.getcwd(), mountpoint.split("/")[-1]))
        return
    print(status())
    print(f"Create ram disk with {block_size=}*{num_blocks=} = {block_size * num_blocks / 1024}kib")
    bdev = RAMBlockDev(block_size, num_blocks)
    os.VfsLfs2.mkfs(bdev)
    os.mount(bdev, mountpoint)
    print(status())


if __name__ == "__main__":
    rd_config = config["ramdisk"]
    setup_ramfs(rd_config["mountpoint"], rd_config["block_size"], rd_config["num_blocks"])
