import re
f = open('input.txt')

node_dict = {}

class Node:
    def __init__(self, color):
        self.color = color
        self.inners = []
        self.parents = []

for line in f.readlines():
    l = re.sub('bags contain ', '', line)
    l = re.sub(' bag(s,)?(s.)?(\.)?', '', l)
    l = re.sub('no other', '', l)
    cols = l.split()

    outer_bag = cols[0] + cols[1]

    if not outer_bag in node_dict:
        node_dict[outer_bag] = Node(outer_bag)

    node = node_dict[outer_bag]

    if len(cols) > 2:
        for i in range(2,len(cols), 3):
            count = int(cols[i])
            inner_bag = cols[i+1] + cols[i+2].replace(',', '')

            if not inner_bag in node_dict:
                node_dict[inner_bag] = Node(inner_bag)

            inner_node = node_dict[inner_bag]
            inner_node.parents.append(node)
            node.inners.append((inner_node, count))

def parent_counter(color, col_dict):
    for parent in node_dict[color].parents:
        col_dict.add(parent.color)
        parent_counter(parent.color, col_dict)

def contains_counter(color):
    ct = 1
    for (node, count) in node_dict[color].inners:
        ct += count * contains_counter(node.color)
    return ct

colors = set()
parent_counter('shinygold', colors)
print(len(colors))
print(contains_counter('shinygold') - 1)
