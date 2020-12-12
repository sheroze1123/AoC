directions = [line.strip('\n') for line in open('input.txt').readlines()]

curx = 0
cury = 0
rot = 90

wpx = 10
wpy = 1
wcx = 0
wcy = 0

for inst in directions:
    tag = inst[0]
    n = int(inst[1:])

    if tag == 'N':
        cury += n
        wpy += n
    elif tag == 'E':
        curx += n
        wpx += n
    elif tag == 'W':
        curx -= n
        wpx -= n
    elif tag == 'S':
        cury -= n
        wpy -= n
    elif tag == 'L':
        dq = int(n/90) % 4
        
        if dq == 1:
            tmp = wpx
            wpx = -wpy
            wpy = tmp
        elif dq == 2:
            wpx = -wpx
            wpy = -wpy
        elif dq == 3:
            tmp = wpx
            wpx = wpy
            wpy = -tmp 
        else:
            import pdb; pdb.set_trace()
        
        rot -= n
        rot = rot % 360
    elif tag == 'R':
        dq = int(n/90) % 4
        
        if dq == 1:
            tmp = wpx
            wpx = wpy
            wpy = -tmp
        elif dq == 2:
            wpx = -wpx
            wpy = -wpy
        elif dq == 3:
            tmp = wpx
            wpx = -wpy
            wpy = tmp 
        else:
            import pdb; pdb.set_trace()

        rot += n
        rot = rot % 360
    elif tag == 'F':
        if 45 <= rot <= 135:
            curx += n
        elif 135 < rot <= 225:
            cury -= n
        elif 225 < rot <= 315:
            curx -= n
        elif (rot < 360) or (rot >= 0):
            cury += n
        else:
            import pdb; pdb.set_trace()

        wcx += (n * wpx)
        wcy += (n * wpy)
    else:
        import pdb; pdb.set_trace()

print(f"M distance: {abs(curx) + abs(cury)}")
print(f"M distance2: {abs(wcx) + abs(wcy)}")
