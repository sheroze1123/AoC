nums = [int(line) for line in open('input.txt').readlines()]

inv_num = None

for i in range(25, len(nums)):
    sum_found = False
    for j in range(1, 26):
        for k in range(j+1, 26):
            #  import pdb; pdb.set_trace()
            if (nums[i-j] + nums[i-k]) == nums[i]:
                sum_found = True
                break
        if sum_found:
            break

    if not sum_found:
        print(nums[i])
        inv_num = nums[i]
        break

b = 0
e = 2

while e < len(nums):
    s = sum(nums[b:e])
    if s == inv_num:
        print(f"Weakness {min(nums[b:e]) + max(nums[b:e])}")
        break
    elif s > inv_num:
        if (b - e) == 2:
            e += 1
        else:
            b += 1
    else:
        e += 1
    
