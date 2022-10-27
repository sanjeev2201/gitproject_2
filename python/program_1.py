"""Given an integer array, one element occurs even number of times and all others have odd occurrences.
Find the element with even occurrences.
    1. input = [1,2,2,2,3,2,3,3,4,4,4,5,4,4] : output = 2
    2. input = [1,2,32,634,664,32] : output = 32
"""


def even_occurrence(lst):
    d = {}
    for i in lst:
        d[i] = d.get(i, 0) + 1
    for k, v in d.items():
        if v % 2 == 0:
            print("Output:", k)


l1 = [1, 2, 2, 2, 3, 2, 3, 3, 4, 4, 4, 5, 4, 4]
even_occurrence(l1)
l2 = [1, 2, 32, 634, 664, 32]
even_occurrence(l2)
print(".................... program 2....................")
"""1. Given an integer array, output all unique pairs that sum up to a specific value 𝑘
    1. input = [3, 4, 5, 6, 7] and k = 10 : output = [(4, 6), (3, 7)]
    2. input = [3, 4, 5, 4, 4] and k = 8 : output is [(3, 5)]"""
lst1 = [3, 4, 5, 6, 7]
k1 = 10
lst2 = [3, 4, 5, 4, 4]
k2 = 8


def Unique_Pair(lst, k):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] != lst[j]:
                if lst[i] + lst[j] == k:
                    print("({},{})".format(lst[i], lst[j]))


Unique_Pair(lst1, k1)
print("........................")
Unique_Pair(lst2, k2)

print("i am updating new code")
print("i am changing code second time")
