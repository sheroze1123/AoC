nums = [18,8,0,5,4,1,20]

d = {}
d[18] = 1
d[8] = 2
d[0] = 3
d[5] = 4
d[4] = 5
d[1] = 6
d[20] = 7

idx = 8
nn = 0

while idx < 30000000:
    #  print(nn)
    if idx % 10000 == 0:
        print(nn)
    if nn in d:
        tmp = d[nn]
        d[nn] = idx
        nn = idx - tmp
    else:
        d[nn] = idx
        nn = 0
    idx += 1

print(nn)
