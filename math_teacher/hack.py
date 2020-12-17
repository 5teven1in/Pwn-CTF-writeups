from z3 import *
from pwn import *

ip = "140.110.112.77"
port = 9003

r = remote(ip, port)

while True:
    x = Int('x')
    y = Int('y')
    s = Solver()
    for _ in range(2):
        eq = r.recvline().replace(b"=", b"==")
        if b"=" not in eq:
            print(eq)
        else:
            s.add(eval(eq))
    if s.check() == sat:
        m = s.model()
        r.sendlineafter("=", str(m[x]))
        r.sendlineafter("=", str(m[y]))

r.interactive()
