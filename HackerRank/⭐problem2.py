"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=false

arr = map(int, input().split())

"""

"""
You don't create an array this way, you create an object that will provide you the objects 
once you iterate over them. Meaning as in a for loop

for v in arr:
    do something with v

or when you would create another sequence from it, like with list()

my_list = list(arr)

the point is that with a list you create a structure in RAM that will hold all the items upfront, 
which is often not what you actually need per se, so map allows you to simply define what you want 
(that takes no CPU or extra storage space) and only performs the actions when needed. 
If you do you need this as a list then a comprehension is preferable over map:

mylist = [int(n) for n in input.split()]

Sidenote: Python doesn't have a regular 'array', it has lists for ordered sequences that can be indexed. 
It does have specialized array for numerical values of a specific type but that's more oriented for low-level 
applications or for interfacing to other systems that need those kind of statically typed arrays.
"""

n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
print(arr[-2])

