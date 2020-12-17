import numpy as np
f = open('input.txt')

intervals = []
my_ticket = None
nearby_tickets = []
parsing_idx = 0

for line in f.readlines():
    if parsing_idx < 20:
        fields = line.split()
        frange = fields[-3].split('-')
        lrange = fields[-1].split('-')
        intervals.append([int(frange[0]), int(frange[1])])
        intervals.append([int(lrange[0]), int(lrange[1])])
    elif parsing_idx == 22:
        my_ticket = list(map(int, line.strip('\n').split(',')))
    elif parsing_idx >= 25:
        nearby_tickets.append(list(map(int, line.strip('\n').split(','))))
    parsing_idx += 1

def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    prev_b = sorted_intervals[0][0]
    prev_e = sorted_intervals[0][1]
    for interval in sorted_intervals[1:]:
        if interval[0] < prev_e:
            prev_e = interval[1]
        else:
            merged.append([prev_b, prev_e])
            prev_b = interval[0]
            prev_e = interval[1]

    if len(merged) == 0:
        merged.append([prev_b, prev_e])
    return merged

def interval_check(val, ints):
    inside = False
    for interval in ints:
        if val >= interval[0] and val <= interval[1]:
            inside = True
            break
        elif val < interval[0]:
            break
    return inside

merged_intervals = merge(intervals)
sum_inv = 0
valid_tickets = []

for ticket in nearby_tickets:
    valid = True
    for f_val in ticket:
        if not interval_check(f_val, merged_intervals):
            valid = False
            sum_inv += f_val
    if valid:
        valid_tickets.append(ticket)
print(f"Part 1: {sum_inv}")

valid_tickets.append(my_ticket)
valid_tickets = np.array(valid_tickets)
n_f = int(len(intervals)/2)
valid = np.zeros((n_f, n_f), dtype=bool)

for f_idx in range(n_f):
    first_interval = np.logical_and(valid_tickets >= intervals[2*f_idx][0], \
                                    valid_tickets <= intervals[2*f_idx][1])
    second_interval = np.logical_and(valid_tickets >= intervals[2*f_idx+1][0], \
                                    valid_tickets <= intervals[2*f_idx+1][1])

    valid[f_idx, :] = np.all(np.logical_or(first_interval, second_interval), axis=0)

field_assignments = [None for _ in range(20)]
occupied = [False for _ in range(20)]
found = 0
while found < 20:
    for i in range(20):
        possible = np.argwhere(np.logical_and(valid[:,i], np.logical_not(occupied))).flatten()
        if len(possible) == 1:
            field_assignments[i] = possible[0]
            occupied[possible[0]] = True
            found += 1

ordred_ticket = np.zeros((20,))
ordred_ticket[field_assignments] = my_ticket
print(f"Part 2: {np.prod(ordred_ticket[:6])}")
