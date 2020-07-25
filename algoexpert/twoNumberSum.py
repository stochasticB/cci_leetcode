array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


def my_twoNumberSum(array, targetSum):
    l = []

    for i in array:
        if targetSum - i in array:
            l.append(i)

    print(l)

my_twoNumberSum(array,targetSum)