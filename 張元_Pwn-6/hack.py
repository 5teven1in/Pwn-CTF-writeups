from pwn import *

ip = "140.110.112.77"
port = 2116

r = remote(ip, port)
# r = process("./pwntools")

r.sendlineafter(")", p32(0x79487FF))
r.recvuntil(".\n")

for _ in range(1000):
    res = r.recvuntil("?").split()
    a, b = int(res[0]), int(res[2])
    op = res[1]
    if op == b"+":
        r.sendline(str(a + b))
    elif op == b"-":
        r.sendline(str(a - b))
    elif op == b"*":
        r.sendline(str(a * b))

r.interactive()
