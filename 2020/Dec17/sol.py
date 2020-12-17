import numpy as np
from copy import deepcopy

init = np.array([[c == '#' for c in line.strip('\n')] for line in open('input.txt').readlines()])
bc = 6
final_dim = 2*bc + len(init)
state = np.zeros((final_dim, final_dim, 2*bc+1), dtype=bool)

state[6:-6, 6:-6, bc] = init
statecopy = deepcopy(state)
curstate = state
nstate = statecopy

for cycle in range(bc):
    for xx in range(final_dim):
        for yy in range(final_dim):
            for zz in range(2*bc+1):
                neigh = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        for k in [-1, 0, 1]:
                            if ((0 <= xx+i < final_dim) and (0 <= yy+j < final_dim) and \
                                    (0 <= zz + k < 2*bc+1)) and not (i==0 and j==0 and k==0):
                                if curstate[xx+i, yy+j, zz+k]:
                                    neigh += 1
                if curstate[xx, yy, zz] and not (2 <= neigh <= 3):
                    nstate[xx, yy, zz] = False
                elif not curstate[xx, yy, zz] and neigh == 3:
                    nstate[xx, yy, zz] = True
                else:
                    nstate[xx, yy, zz] = curstate[xx, yy, zz]
    tmp = curstate
    curstate = nstate
    nstate = tmp

active = 0
for xx in range(final_dim):
    for yy in range(final_dim):
        for zz in range(2*bc+1):
            if curstate[xx, yy, zz]:
                active += 1

print(active)

state = np.zeros((final_dim, final_dim, 2*bc+1, 2*bc+1), dtype=bool)

state[6:-6, 6:-6, bc, bc] = init
statecopy = deepcopy(state)
curstate = state
nstate = statecopy

for cycle in range(bc):
    for xx in range(final_dim):
        for yy in range(final_dim):
            for zz in range(2*bc+1):
                for ww in range(2*bc+1):
                    neigh = 0
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            for k in [-1, 0, 1]:
                                for l in [-1, 0, 1]:
                                    if ((0 <= xx+i < final_dim) and \
                                            (0 <= yy+j < final_dim) and \
                                            (0 <= zz + k < 2*bc+1) and \
                                            (0 <= ww + l < 2*bc+1)) and not \
                                            (i==0 and j==0 and k==0 and l==0):
                                        if curstate[xx+i, yy+j, zz+k, ww+l]:
                                            neigh += 1
                    if curstate[xx, yy, zz, ww] and not (2 <= neigh <= 3):
                        nstate[xx, yy, zz, ww] = False
                    elif not curstate[xx, yy, zz, ww] and neigh == 3:
                        nstate[xx, yy, zz, ww] = True
                    else:
                        nstate[xx, yy, zz, ww] = curstate[xx, yy, zz, ww]
    tmp = curstate
    curstate = nstate
    nstate = tmp

active = 0
for xx in range(final_dim):
    for yy in range(final_dim):
        for zz in range(2*bc+1):
            for ww in range(2*bc+1):
                if curstate[xx, yy, zz, ww]:
                    active += 1

print(active)
