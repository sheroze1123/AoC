import numpy as np

tiles = [(int(line.split(':')[0].split(' ')[1]), \
        [[c=='#' for c in r] for r in line.split(':')[1].strip('\n').split('\n')])\
        for line in open('input.txt').read().split('\n\n')]

numorder = [k for (k,v) in tiles]
adj_mat = np.zeros((len(numorder), len(numorder)), dtype=bool)

def append_if(d, k, v):
    if k in d:
        d[k].append(v)
    else:
        d[k] = [v]

tm = {}
em = {}
tem = {}
for (num, square) in tiles:
    tm[num] = np.array(square)
    t = ''.join([str(c) for c in tm[num][0,:].astype(int)])
    b = ''.join([str(c) for c in tm[num][-1,:].astype(int)])
    r = ''.join([str(c) for c in tm[num][:,-1].astype(int)])
    l = ''.join([str(c) for c in tm[num][:,0].astype(int)])
    
    append_if(em, t, num)
    append_if(em, b, num)
    append_if(em, l, num)
    append_if(em, r, num)
    append_if(em, t[::-1], num)
    append_if(em, b[::-1], num)
    append_if(em, l[::-1], num)
    append_if(em, r[::-1], num)
    tem[num] = [t, b, l, r, t[::-1], b[::-1], l[::-1], r[::-1]]

ecm = {}
for values in em.values():
    for num in values:
        if len(values) == 2:
            id1 = numorder.index(values[0])
            id2 = numorder.index(values[1])
            adj_mat[id1, id2] = True
            adj_mat[id2, id1] = True
        if num in ecm:
            ecm[num].append(len(values))
        else:
            ecm[num] = [len(values)]

prod = 1
outer_pieces = []
corner_pieces = []
for (key, value) in ecm.items():
    neigh_count = value.count(2)
    if neigh_count == 4:
        # corners
        prod *= key
        corner_pieces.append(key)
        outer_pieces.append(key)
    elif neigh_count == 6:
        # edges
        outer_pieces.append(key)

print(prod)

#build image
tile = corner_pieces[0]
tile_side = len(tiles[0][1])
nside = int(np.sqrt(len(numorder)))
tilegrid = np.zeros((nside, nside), dtype=int)
tilegrid[0][0] = tile
placed = {}
placed[tile] = True

for i in range(1, nside):
    tileidx = numorder.index(tile)
    neighs = np.argwhere(adj_mat[tileidx]).flatten()
    pos = [numorder[n] for n in neighs if ((not numorder[n] in placed) and (numorder[n] in outer_pieces))]
    tile = pos[0]
    tilegrid[0][i] = tile
    placed[tile] = True

tile = corner_pieces[0]
for i in range(1, nside):
    tileidx = numorder.index(tile)
    neighs = np.argwhere(adj_mat[tileidx]).flatten()
    pos = [numorder[n] for n in neighs if ((not numorder[n] in placed) and (numorder[n] in outer_pieces))]
    tile = pos[0]
    tilegrid[i][0] = tile
    placed[tile] = True

tile = tilegrid[-1,0]
for i in range(1, nside):
    tileidx = numorder.index(tile)
    neighs = np.argwhere(adj_mat[tileidx]).flatten()
    pos = [numorder[n] for n in neighs if ((not numorder[n] in placed) and (numorder[n] in outer_pieces))]
    tile = pos[0]
    tilegrid[-1][i] = tile
    placed[tile] = True

tile = tilegrid[0,-1]
for i in range(1, nside-1):
    tileidx = numorder.index(tile)
    neighs = np.argwhere(adj_mat[tileidx]).flatten()
    pos = [numorder[n] for n in neighs if ((not numorder[n] in placed) and (numorder[n] in outer_pieces))]
    tile = pos[0]
    tilegrid[i][-1] = tile
    placed[tile] = True

for i in range(1, nside-1):
    for j in range(1, nside-1):
        above = tilegrid[i-1][j]
        left = tilegrid[i][j-1]
        aidx = numorder.index(above)
        lidx = numorder.index(left)
        above_neighs = np.argwhere(adj_mat[aidx]).flatten()
        left_neighs = np.argwhere(adj_mat[lidx]).flatten()
        candidate = [numorder[n] for n in above_neighs if ((n in left_neighs) and (numorder[n] not in placed))]
        tilegrid[i][j] = candidate[0]
        placed[candidate[0]] = True

image = np.zeros((tile_side*nside, tile_side*nside), dtype=bool)
image[0:tile_side, 0:tile_side] = tm[tilegrid[0][0]].T

def transformbot(sq, code):
    if code == 0:
        return sq
    elif code == 1:
        return np.flipud(sq)
    elif code == 2:
        return sq.T
    elif code == 3:
        return np.rot90(sq)
    elif code == 4:
        return np.fliplr(sq)
    elif code == 5:
        return np.rot90(sq, 2)
    elif code == 6:
        return np.rot90(sq, 3)
    elif code == 7:
        return np.fliplr(np.rot90(sq))

import matplotlib.pyplot as plt

# Build left edge
for i in range(1, nside):
    edge = image[(i*tile_side)-1, 0:tile_side]
    eb = ''.join([str(c) for c in edge.astype(int)])
    tile = tilegrid[i,0]
    sq = tm[tile]
    ei = tem[tile].index(eb)
    image[i*tile_side:(i+1)*tile_side, 0:tile_side] = transformbot(sq, ei)

def transformright(sq, code):
    if code == 0:
        return sq.T
    elif code == 1:
        return np.rot90(sq, 3)
    elif code == 2:
        return sq
    elif code == 3:
        return np.fliplr(sq)
    elif code == 4:
        return np.rot90(sq)
    elif code == 5:
        return np.flipud(np.rot90(sq, 3))
    elif code == 6:
        return np.flipud(sq)
    elif code == 7:
        return np.rot90(sq, 2)

for i in range(0, nside):
    for j in range(1, nside):
        edge = image[(i*tile_side):(i+1)*tile_side, (j*tile_side)-1]
        eb = ''.join([str(c) for c in edge.astype(int)])
        tile = tilegrid[i,j]
        sq = tm[tile]
        ei = tem[tile].index(eb)
        image[i*tile_side:(i+1)*tile_side, j*tile_side:(j+1)*tile_side] = \
                transformright(sq, ei)

nts = tile_side - 2
si = np.zeros((nts*nside, nts*nside), dtype=bool)

for i in range(0, nside):
    for j in range(0, nside):
        tile = image[i*tile_side:(i+1)*tile_side, j*tile_side:(j+1)*tile_side]
        si[i*nts:(i+1)*nts,j*nts:(j+1)*nts] = tile[1:-1,1:-1]

monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]

sm = np.array([[c=='#' for c in line] for line in monster])

creature_pounds = np.sum(sm)
total_pounds = np.sum(si)

def findsubarray(suba, a):
    creatures = 0

    for i in range(a.shape[0] - suba.shape[0]):
        for j in range(a.shape[1] - suba.shape[1]):
            search = a[i:i+suba.shape[0], j:j+suba.shape[1]]
            if np.all(search[suba]):
                creatures += 1
    if creatures > 0:
        print (total_pounds - creatures * creature_pounds)


findsubarray(sm, si)
findsubarray(sm, np.rot90(si))
findsubarray(sm, np.rot90(si, 2))
findsubarray(sm, np.rot90(si, 3))
findsubarray(sm, np.flipud(si))
findsubarray(sm, np.fliplr(si))
findsubarray(sm, si.T)
findsubarray(sm, np.fliplr(np.rot90(si)))
