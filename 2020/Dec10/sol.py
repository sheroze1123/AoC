from functools import reduce
nums = [int(line) for line in open('input.txt').readlines()]
s = sorted(nums)
s.insert(0, 0)

j1 = 0
j3 = 0
cont = []
streak = 0

for i in range(len(s)-1):
    diff = s[i+1] - s[i]
    streak += 1
    if diff == 1:
        j1 += 1
    elif diff == 3:
        j3 += 1
        cont.append(streak)
        streak = 0
    else:
        import pdb; pdb.set_trace()

if streak > 0:
    cont.append(streak+1)
j3 += 1

def perm(val):
    if val <= 2:
        return 1
    elif val == 3:
        return 2
    elif val == 4:
        return 4
    elif val == 5:
        return 7

print(j1*j3)
print(reduce(lambda x, y: x*y, map(perm, cont)))

