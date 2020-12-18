expressions = [[char for char in line.strip('\n').replace(' ','')] \
        for line in open('input.txt').readlines()]

def parse(expr, idx):
    accum = None
    if expr[idx] == '(':
        (accum, idx) = parse(expr, idx+1)
    else:
        accum = int(expr[idx])
        idx += 1

    s = False
    m = False

    while idx < len(expr):
        if expr[idx] == ')':
            return (accum, idx+1)
        elif expr[idx] == '+':
            s = True
            idx += 1
        elif expr[idx] == '*':
            m = True
            idx += 1
        elif expr[idx] == '(':
            (p_sum, idx) = parse(expr, idx+1)
            if s:
                accum += p_sum
            elif m:
                accum *= p_sum
            else:
                import pdb; pdb.set_trace()
            s = False
            m = False
        else:
            v = int(expr[idx])
            if s:
                accum += v
            elif m:
                accum *= v
            else:
                import pdb; pdb.set_trace()
            s = False
            m = False
            idx += 1
    return (accum, idx+1)


sum_ans = 0

for expr in expressions:
    (p_sum, _) = parse(expr, 0)
    sum_ans += p_sum
    
print(sum_ans)

def lookbackwards(modified):
    assert modified[-1] == ')'
    openb = 1
    idx = 2
    while openb > 0:
        if modified[-idx] == '(':
            openb -= 1
        elif modified[-idx] == ')':
            openb += 1
        idx += 1
    modified.insert(-(idx-1), '(')

def modifier(expr, idx, modified):
    if expr[idx] == '(':
        modified.append('(')
        idx = modifier(expr, idx+1, modified)
    else:
        modified.append(expr[idx])
        idx += 1

    while idx < len(expr):
        if expr[idx] == ')':
            modified.append(')')
            return idx+1
        elif expr[idx] == '*':
            modified.append('*')
            idx += 1
        elif expr[idx] == '(':
            modified.append('(')
            idx = modifier(expr, idx+1, modified)
        elif expr[idx] == '+':
            if modified[-1] == ')':
                lookbackwards(modified)
            else:
                modified.insert(-1, '(')
            modified.append('+')

            if expr[idx+1] == '(':
                modified.append('(')
                idx = modifier(expr, idx+2, modified)
            else:
                modified.append(expr[idx+1])
                idx += 2
            modified.append(')')
        else:
            modified.append(expr[idx])
            idx += 1
    return idx

sum_ans = 0

for expr in expressions:
    modified_expr = []
    modifier(expr, 0, modified_expr)
    (p_sum, _) = parse(modified_expr, 0)
    sum_ans += p_sum
    
print(sum_ans)
