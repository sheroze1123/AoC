f = open('input.txt')

mask = None
ones = None
zeros = None
mem = {}
mem2 = {}

def write(memory, bmask, value):
    if 'X' in bmask:
        write(memory, bmask.replace('X', '1', 1), value)
        write(memory, bmask.replace('X', '0', 1), value)
    else:
        memory[int(bmask, 2)] = value

for line in f.readlines():
    lhs, eq, data = line.strip('\n').split()

    if lhs == 'mask':
        mask = data
        ones = int(data.replace('X', '0'), 2)
        zeros = int(data.replace('X', '1'), 2)
    else:
        val = int(data)
        masked = (val & zeros)
        masked = (masked | ones)
        mem[lhs] = masked

        loc = int(lhs[4:-1]) | int(mask.replace('X', '0'), 2)
        
        bmask = format(loc, f'0{len(mask)}b')
        for ii in range(len(mask)):
            if mask[ii] == 'X':
                bmask = (bmask[:ii] + 'X' + bmask[ii+1:])

        write(mem2, bmask, val)

print(sum(mem.values()))
print(sum(mem2.values()))

