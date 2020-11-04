'''
> given two strings, write a method to decide if one is a permutation of the other
> permutation - a way, especially one of several possible variations, in which a set or number of things can be ordered or arranged.
'''

str1 = 'abc'
str2 = 'cab'


def my_solution(s1,s2):
    for char in s1:
        print(char)


#my_solution(s1)


def sum_stack(n):
    total = 0
    if n <= 0:
        return 0
    else:
        print(n + sum_stack(n-1))
    #print(1+2)
sum_stack(5)
#15= 5 + 4 + 3 + 2 + 1