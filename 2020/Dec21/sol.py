import re
f = open('input.txt')
m = {}
counts = {}

for line in f.readlines():
    ing, al = line.split('(')
    ingredients = ing.split()
    allergens = re.findall('\w+', al)[1:]
    for allergen in allergens:
        if allergen in m:
            m[allergen] = m[allergen].intersection(set(ingredients))
        else:
            m[allergen] = set(ingredients)
    for ingredient in ingredients:
        if ingredient in counts:
            counts[ingredient] += 1
        else:
            counts[ingredient] = 1

possible_allergens = set()

for v in m.values():
    possible_allergens = possible_allergens.union(v)

noa = 0
for (k, v) in counts.items():
    if k not in possible_allergens:
        noa += counts[k]

print(noa)

num_a = len(m.keys())

found = 0
assngd = set()
f = {}
while found < num_a:
    for (k, v) in m.items():
        m[k] = m[k] - assngd
        if len(m[k]) == 1:
            al = m[k].pop()
            assngd.add(al)
            f[k] = al
            found += 1

cdil = ""
for key in sorted(f):
    cdil += (f[key] + ",")

print(cdil)
import pdb; pdb.set_trace()
