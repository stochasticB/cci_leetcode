'''
    > 1.1 Is Unique: implement an algorithm to determine if a string has all unique characters.
    > what if you cannot use additional data structures?
    > Hint #1: use a hash table (dictionary)
    > Hint #2: could a bit vector be useful?
    > Hint #3: can you solve it in O(N logN) time?
    > 1st q to ask your interviewer: is the string an ASCII or Unicode? Assume ASCII, if not, you'll need to increase the size storage
    > Git Push: 1) CTRL + ALT + K - commit, 2) CTRL + SHIFT + K - push

'''

s1 = 'abcdefg'
s2 = 'aabcdef'


def my_is_unique(s):
    if s == '':
        print('Please enter a string')
        exit()
        # input()
        
    char_dic = {}
    for char in s:
        if char not in char_dic:
            char_dic[char] = 1
        else:
            char_dic[char] += 1
    
    dict_count = 0
    for x in char_dic:
        dict_count += char_dic[x]

    # print(dict_count)
    if dict_count % len(char_dic) == 0:
        print('String ' + s + 'is unique')
    else:
        print('String ' + s + ' is not unique')


# my_is_unique(s2)


# Sol 1: create an array of booleans, where the flag in index i indicates whether character i in the alphabet is contained in the string
# the second time you see this char you can immediately return false

def sol_1(s):
    if len(s) > 128:    # if the s exceeds the num of unique chars in the alphabet, it isn't unique
        print(False)

    char_set = [False for _ in range(128)] # returns a list of 128 Falses; _ represents a throwaway/iteration value (created by range() function)

    for char in s:
        val = ord(char) # returns an integer representing the unicode character; inverse of the chr()
        if char_set[val]:
            print(False)
            return False
        char_set[val] = True

    print(True)

sol_1(s1)




