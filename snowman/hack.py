from pwn import *

context.arch = "amd64"

r = process("./snowman")

r.sendline("y")

r.interactive()
