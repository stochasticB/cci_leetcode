# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

# [3, 3, 2, 1, 3, 2, 1] --> [1, 1, 2, 2, 3, 3, 3]


def sort_nums_bn(nums):
    return sorted(nums)
    # return nums.sort()


def sort_nums_sol1(nums):
    num_one = 0
    num_two = 0
    num_three = 0

    for n in nums:
        if n == 1:
            num_one += 1
        if n == 2:
            num_two += 1
        if n == 3:
            num_three += 1

    return [1]*num_one + [2]*num_two + [3]*num_three


def sort_nums_sol2(nums):
    one_idx = 0
    three_idx = len(nums) - 1   # 6
    idx = 0

    while idx <= three_idx:     # while 0 <= 6
        if nums[idx] == 1:      # nums[0] == 1:
            nums[idx], nums[one_idx] = nums[one_idx], nums[idx]
            idx += 1
            one_idx += 1

        elif nums[idx] == 2:
            idx += 1
        elif nums[idx] == 3:
            nums[idx], nums[three_idx] = nums[three_idx], nums[idx]
            three_idx -= 1
    return nums

# print([5]*5 + [1]*2)
# print(sort_nums_bn([3, 3, 2, 1, 3, 2, 1]))
#print(sort_nums_sol1([3, 3, 2, 1, 3, 2, 1]))
# print (len([3, 3, 2, 1, 3, 2, 1]) - 1)
# print(sort_nums_sol2([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]

l = [1, 2, 3]
print('Original list: ', l)
l[0], l[1] = l[1], l[0]
# [1, 2, 3] --> l[0], l[1] = l[1], l[0] --> [2, 1, 3]
print('Modified list: ', l)

# Notes
# 1. functions and variables should all be lowercase. Use underscore(_) to provide clarity
# 2. functions like indentations that are multiple of fours, so just use tab
# 3. Python sorting: 2 options - [list.sort() method ->  it modifies the list-in place, sorted(list) function]
# 4. when using a .py method, its list period sort parantheses
# 5. lets say I want a list of 100 5's. how do i do that? [5] * 100 = [5, 5, 5, ... ,5]
# 6. you can combine lists by the plus sign: [1,2,3] + [4,5] = [1,2,3,4,5]
# 7. combine #5 and #6: return [1]*num_one + [2]* num_two + [3]*num_three
# 8. # [1, 2, 3] --> l[0], l[1] = l[1], l[0] --> [2, 1, 3]. you can switch the value of two indexed positions