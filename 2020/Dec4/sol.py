import numpy as np
import re

f = open('input.txt')
data = f.read()

passports = np.array([x.split() for x in data.split('\n\n')])
field_count = [len(x) for x in passports]
uniques, counts = np.unique(field_count, return_counts=True)
count_map = dict(zip(uniques, counts))
all_fields = count_map[8]

cid_reg = re.compile('cid:*')
one_less = passports[np.equal(field_count, 7)]

inv_7fields = sum(map(lambda x: len(list(filter(cid_reg.match, x))), one_less))

print(all_fields + count_map[7] - inv_7fields)

fancy_valid = 0
normal_valid = 0
hexmatch = re.compile('^#[0-9a-f]{6}$')
pidmatch = re.compile('^[0-9]{9}$')
cmmatch = re.compile('^1[5-9][0-9]cm$')
inmatch = re.compile('^[5-7][0-9]in$')
eyecols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def between(value, lower, upper):
    return (value >= lower) and (value <= upper)
v = []
for passport in passports:
    if len(passport) >= 7:
        p = {}
        for field in passport:
            key, value = field.split(':')
            p[key] = value

        if not (p.keys() >= {"byr", "eyr", "iyr", "hgt", "hcl", "ecl", "pid"}):
            continue

        normal_valid += 1
        
        if not between(int(p['byr']), 1920, 2002):
            continue

        if not between(int(p['iyr']), 2010, 2020):
            continue

        if not between(int(p['eyr']), 2020, 2030):
            continue

        if not hexmatch.search(p['hcl']):
            continue

        if not pidmatch.search(p['pid']):
            continue

        if not p['ecl'] in eyecols:
            continue

        if cmmatch.search(p['hgt']):
            val = int(p['hgt'][:-2])
            if not between(val, 150, 193):
                continue
        elif inmatch.search(p['hgt']):
            val = int(p['hgt'][:-2])
            if not between(val, 59, 76):
                continue
        else:
            continue

        fancy_valid += 1

print(f"Fancy valid: {fancy_valid}")
print(f"Normal valid: {normal_valid}")
