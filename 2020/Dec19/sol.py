import re
f = open('input.txt')

parsing_messages = False
rule_dict = {}
regex = None
regex2 = None

def gen_regex(key, regex):
    if not type(rule_dict[key]) is list:
        regex.append(rule_dict[key])
    else:
        nested_rules = rule_dict[key]
        if len(nested_rules) == 1:
            for k in nested_rules[0]:
                gen_regex(k, regex)
        else:
            regex.append('(')
            for rule in nested_rules:
                for k in rule:
                    gen_regex(k, regex)
                regex.append('|')
            regex.pop()
            regex.append(')')

def gen_regex2(key, regex):
    if not type(rule_dict[key]) is list:
        regex.append(rule_dict[key])
    else:
        if key == '8':
            regex.append('(')
            gen_regex2('42', regex)
            regex.append(')')
            regex.append('+')
        elif key == '11':
            regex.append('(')
            gen_regex2('42', regex)
            regex.append(')')
            regex.append('{x}')
            regex.append('(')
            gen_regex2('31', regex)
            regex.append(')')
            regex.append('{x}')
        else:
            nested_rules = rule_dict[key]
            if len(nested_rules) == 1:
                for k in nested_rules[0]:
                    gen_regex2(k, regex)
            else:
                regex.append('(')
                for rule in nested_rules:
                    for k in rule:
                        gen_regex2(k, regex)
                    regex.append('|')
                regex.pop()
                regex.append(')')

match_count = 0
match_count2 = 0
for line in f.readlines():
    if line == '\n':
        parsing_messages = True
        reg = ['^']
        reg2 = ['^']
        gen_regex('0', reg)
        gen_regex2('0', reg2)
        reg.append('$')
        reg2.append('$')
        regex = ''.join(reg)
        regex2 = ''.join(reg2)
    elif not parsing_messages:
        if re.match('\d+: "\w"', line.strip('\n')):
            rule_dict[re.search('\d+', line)[0]] = line[-3]
        else:
            nums = re.split('[:\|]', line.strip('\n'))
            rule_dict[nums[0]] = []
            for val in nums[1:]:
                rule_dict[nums[0]].append(val.split())
    else:
        if re.match(regex, line.strip('\n')):
            match_count += 1
        for i in range(1,10):
            proper_regex = regex2.replace('x',str(i))
            if re.match(proper_regex, line.strip('\n')):
                match_count2 += 1
                break

print(match_count)
print(match_count2)
