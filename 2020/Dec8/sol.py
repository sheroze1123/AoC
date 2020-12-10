import copy
ops = [line.strip().split() for line in open('input.txt').readlines()]

idx = 0
acc = 0

instructions = {}

def step(acc, idx, os, insts):
    insts[idx] = os[idx]
    instruction, value = os[idx]
    value = int(value)
    if instruction == 'acc':
        acc += value
        idx += 1
    elif instruction == 'jmp':
        idx += value
    else:
        idx += 1
    
    return acc, idx

while idx not in instructions:
    acc, idx = step(acc, idx, ops, instructions)
print(acc)

loop_begin = idx
_, idx = step(acc, idx, ops, instructions)
loop = [ops[idx]]
loopidxs = [idx]

while idx != loop_begin:
    _, idx = step(acc, idx, ops, instructions)
    loop.append(ops[idx])
    loopidxs.append(idx)

def is_loop(o, i):
    a = 0
    seen = {}
    
    while i < len(o):
        _, i = step(a, i, o, seen)
        if i in seen:
            return True
    return False
    
for (instr, idx) in zip(loop, loopidxs):
    opscopy = copy.deepcopy(ops)
    newidx = idx
    if opscopy[idx][0] == 'jmp':
        newidx += 1
        opscopy[idx][0] = 'nop'
    elif opscopy[idx][0] == 'nop':
        newidx += int(opscopy[idx][1])
        opscopy[idx][0] = 'jmp'
    else:
        newidx += 1

    if is_loop(opscopy, newidx):
        continue
    else:
        print(f'Changed idx: {idx}')
        break
acc = 0
idx = 0
insts = {}
while idx not in insts:
    if idx >= len(ops):
        break
    acc, idx = step(acc, idx, opscopy, insts)
print(acc)
