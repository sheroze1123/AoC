import re
f = open('input.txt', 'r')
valid = 0
validv2 = 0

for line in f.readlines():
    bounds, character, password, _ = re.split(': |\s', line)
    lower, upper = map(int, bounds.split('-'))
    char_count = password.count(character)
    if char_count >= lower and char_count <= upper:
        valid += 1
    if (password[lower-1] == character) ^ (password[upper-1] == character):
        validv2 += 1

print(f"Valid characters: {valid}")
print(f"Valid characters (part 2): {validv2}")
