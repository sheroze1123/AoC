import numpy as np
f = open('input.txt')

max_unique = -1
unique_ids = []

for line in f.readlines():
    row = 0
    col = 0
    incr = 64
    col_incr = 4

    for i in range(7):
        if line[i] == 'B':
            row += incr
        incr /= 2
    for j in range(3):
        if line[7 + j] == 'R':
            col += col_incr
        col_incr /= 2

    unique_id = row * 8 + col
    
    unique_ids.append(unique_id)
    if unique_id > max_unique:
        print(f"Row: {row}, Col: {col}")
        print(line)
        max_unique = unique_id

print(max_unique)
print(np.sort(unique_ids))

