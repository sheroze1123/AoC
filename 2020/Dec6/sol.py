from functools import reduce
f = open('input.txt')
data = f.read()
forms = data.split('\n\n')

def intersect(list_of_sets):
    return reduce(lambda x,y: x.intersection(y), list_of_sets)

sol1 = sum([len(set([char for char in form.replace('\n','')])) for form in forms])

sol2 = sum([len(intersect([set([char for char in answer]) \
        for answer in form.strip('\n').split('\n')])) \
        for form in forms])
print(f"Solution 1: {sol1}")
print(f"Solution 2: {sol2}")

