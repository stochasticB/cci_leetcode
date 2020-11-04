# 001 - Add two numbers as a linked list

# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a
# single digit. Add the two numbers and return it as a linked list.

# ex.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Notes
# 1. static (using the @staticmethod decorator). ... Hence the method could be static, i.e.
#   callable without passing a class instance or without even having created a class instance.
# 2. functions should be lowercase

class ListNode(object):
    # Definition for singly-linked list.
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
   def addtwonumbers_bn(self, l1, l2, c = 0):
    x1 = int(str(l1.next.next.val) + str(l1.next.val) + str(l1.val))
    x2 = int(str(l2.next.next.val) + str(l2.next.val) + str(l2.val))
    x3 = str(x1 + x2)

    l3 = ListNode(x3[2])
    l3.next = ListNode(x3[1])
    l3.next.next = ListNode(x3[0])

    #print(l3.val, l3.next.val, l3.next.next.val)
    print(l3)

  def addTwoNumbersSolution(self,l1,l2):
    return self.addTwoNumbersRecursive(11, 12, 0)

  def addTwoNumbersRecursive(self, l1, l2, c):
    val = l1.val + l2.val + c
    c = val/10
    ret = ListNode(val%10)

    if l1.next != None or l2.next != None:
      if not l1.next:
        l1.next = ListNode(0)
      if not l2.next:
        l2.next = ListNode(0)
      ret.next = self.addTwoNumbersRecursive(l1.next, l2.next, c)
    return ret

  def addTwoNumbersIterative(self, l1, l2):
    a = l1
    b = l2
    c = 0
    ret = current = None

    while a or b:
      val = a.val + b.val + c
      c = val / 10
      if not current:
        ret = current = ListNode(val % 10)
      else:
        current.next = ListNode(val % 10)
        current = current.next

      if a.next or b.next:
       if not a.next:
          a.next = ListNode(0)
        if not b.next:
          b.next = ListNode(0)
    a = a.next
    b = b.next
    return ret

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# result = Solution().addtwonumbers_bn(l1, l2)
result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val),
  result = result.next
# 7 0 8

# SOLUTION
# This can be done recursively, keeping track of the carryover value as a parameter.

# The algorithm iterates O(max(m,n)) times, so it is linear time.
# It can use linear space, as the recursion stack space will iterate O(max(m,n)) times as well.

# A fun exercise is to also do the iterative version, which you should try to write!
# The answer for this as well is included below. It is also linear time/space complexity
# because of the single iteration through each linked list and the construction of the result.