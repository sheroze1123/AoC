from copy import deepcopy
grid = [[char for char in line.strip('\n')] for line in open('input.txt').readlines()]
gridcopy = deepcopy(grid)

def countadj(grid, i, j):
    count = 0
    for ni in [-1, 0, 1]:
        for nj in [-1, 0, 1]:
            nwi = i + ni
            nwj = j + nj
            if nwi == i and nwj == j:
                continue
            if 0 <= nwi < len(grid) and 0 <= nwj < len(grid[i]) and grid[nwi][nwj] == '#':
                count += 1
    return count

def visibility(grid, i, j):
    count = 0
    for ni in [-1, 0, 1]:
        for nj in [-1, 0, 1]:
            nwi = i + ni
            nwj = j + nj
            if nwi == i and nwj == j:
                continue

            found = False
            while not found:
                if nwi < 0 or nwi >= len(grid) or nwj < 0 or nwj >= len(grid[i]):
                    # out of bounds
                    break

                if grid[nwi][nwj] == '#':
                    found = True
                    count += 1
                elif grid[nwi][nwj] == 'L':
                    found = True
                else:
                    nwi += ni
                    nwj += nj
    return count

cgrid = grid
ngrid = gridcopy 

change = True

while change:
    change = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #  adjc = countadj(cgrid, i, j)
            adjc = visibility(cgrid, i, j)

            if adjc == 0 and cgrid[i][j] == 'L':
                ngrid[i][j] = '#'
                change = True
            elif adjc >= 5 and cgrid[i][j] == '#':
                ngrid[i][j] = 'L'
                change = True
            else:
                ngrid[i][j] = cgrid[i][j]

    tmp = cgrid
    cgrid = ngrid
    ngrid = tmp

occ = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if cgrid[i][j] == '#':
            occ += 1

print(occ)
import pdb; pdb.set_trace()
