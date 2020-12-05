import numpy as np
f = open('input.txt', 'r')

tree_map = []
for line in f.readlines():
    tree_map.append([char for char in line.strip()])
graph = np.array(tree_map)

di_s = [1,1,1,1,2]
dj_s = [1,3,5,7,1]
tree_counts = []

for (di, dj) in zip(di_s, dj_s):
    i = 0
    j = 0
    tree_count = 0
    while i < graph.shape[0]:
        if graph[i, j] == '#':
            tree_count += 1
        i += di
        j += dj
        j = j % graph.shape[1]
    tree_counts.append(tree_count)

print(f"Tree counts: {tree_counts}")
print(f"Product: {np.prod(tree_counts)}")
