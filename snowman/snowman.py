'''
Just a guide for angr.
You can solve the challenge (asciiart) by these skill.
'''
import angr
proj = angr.Project('snowman')
snowman_adr = proj.loader.find_symbol('snowman').rebased_addr
print(f'snowman in: {hex(snowman_adr)}')
simgr = proj.factory.simgr()
simgr.explore(find=0x400662)
#simgr.explore(find=0x40066e)
snowman_y = simgr.found[0]
ans = snowman_y.mem[snowman_y.regs.rbp-0xa].uint8_t.resolved
ans_0 = snowman_y.solver.eval(ans)
print(f'ans[0] = {chr(ans_0)} ({ans_0})')
print('stdout:', snowman_y.posix.dumps(1))
print('stdin:', snowman_y.posix.dumps(0))
print(simgr)
simgr.move(from_stash='active', to_stash='garbage')
print(simgr)
simgr.move(from_stash='found', to_stash='active')
print(simgr)
simgr.explore(find=0x400617)
print(simgr.found[0].posix.dumps(1))
