# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

# Example: Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.

def two_sum_bn(list, k):
  for i in list:
      ans = k - i
      if ans in list:
          print('i = ',i, 'k = ',k, 'ans = ', ans )
          return True
      # print(i,k, ans)

# print(two_sum([4,7,1,-3,2], 5))
print(two_sum_bn([3, 5, 2, -4, 8, 11], 8))
# True

# Try to do it in a single pass of the list.
# The naive/brute force solution is simply to have a nested for-loop,
# iterating over all possible pairs in the list. Then, if at any point,
# the sum is equal to k, return true. If the for loops terminate, return false.

def two_sum(list, k):
  for i in range(len(list)):
    for j in range(len(list)):
      if i != j and list[i] + list[j] == k:
        return True
  return False

print two_sum([4,7,1,-3,2], 5)
# True
# This solution has a time complexity of O(N2) due to the nested loop.

#A more optimal solution involves using a hash set. Iterate through the list, and for each element,
# first check if k - curr_element is in the set. If not, add curr_element to the set and proceed to the
# next element. If you reach the end of the list, no such pair exists, so return False.

def two_sum(list, k):
    seen = set()
    for num in list:
        if k - num in seen:
            return True
        seen.add(num)
    return False




# This solution does a single pass and thus has a time complexity of O(N),
# but also has a space complexity of O(N) due to the set.

# A third solution would be to first sort the list, and then iterate through it.
# While iterating through each element, do a binary search to find if the required complement
# of the current element (to make the sum k) exists in the list.

# This solution has a time complexity of O(N log N) because sorting is N log N, and then in the loop,
# we perform a binary search for each element which is also N log N. However, this solution has a space
# complexity of O(1).

from bisect import bisect_left


def two_sum(list, K):
    list.sort()

    for i in range(len(list)):
        target = K - list[i]
        j = binary_search(list, target)
        if j == -1:
            continue
        elif j != i:
            return True

        elif j + 1 < len(list) and list[j + 1] == target:
            return True
        elif j - 1 >= 0 and list[j - 1] == target:
            return True
    return False


def binary_search(list, target):
    low = 0
    high = len(list)
    index = bisect_left(list, target, low, high)

    if 0 <= index < high and list[index] == target:
        return index
    return -1


print
two_sum([4, 7, 1, -3, 2], 5)
# True
