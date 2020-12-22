from collections import deque
deck = [[int(c) for c in p.strip('\n').split('\n')] for p in open('input.txt').read().split('\n\n')]
p1 = deque(deck[0])
p2 = deque(deck[1])

w1 = False
while len(p1) > 0 and len(p2) > 0:
    p1c = p1.popleft()
    p2c = p2.popleft()

    if p1c > p2c:
        p1.append(p1c)
        p1.append(p2c)
        w1 = True
    else:
        p2.append(p2c)
        p2.append(p1c)
        w1 = False

ans = 0
itr = 1
wd = p2
if w1:
    wd = p1

for i in range(len(wd)):
    ans += (i+1)*wd.pop()

print(f"Part1: {ans}")

def hash(p1, p2):
    s = ""
    for c in p1:
        s += str(c) + ","
    s += "|"
    for c in p2:
        s += str(c) + ","
    return s[:-1]

def play(p1, p2):
    w1 = False
    d = {}
    while len(p1) > 0 and len(p2) > 0:
        if hash(p1,p2) in d:
            # p1 wins
            [p1.append(c) for c in p2]
            return (True, p1)
        d[hash(p1, p2)] = True

        p1c = p1.popleft()
        p2c = p2.popleft()

        if (len(p1) >= p1c) and (len(p2) >= p2c):
            (w1, _) = play(deque(list(p1)[:p1c]), deque(list(p2)[:p2c]))
        else:
            w1 = (p1c > p2c)

        if w1:
            p1.append(p1c)
            p1.append(p2c)
        else:
            p2.append(p2c)
            p2.append(p1c)
    return (w1, p1 if w1 else p2)

(_, cards) = play(deque(deck[0]), deque(deck[1]))
ans = 0
itr = 1
for i in range(len(cards)):
    ans += (i+1)*cards.pop()

print(f"Part2: {ans}")
