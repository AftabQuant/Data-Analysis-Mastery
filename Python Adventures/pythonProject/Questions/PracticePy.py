# power of a number
# x = int(input("Enter The Base : "))
# y = int(input("Enter The Power : "))
# print("Result is :  ",x ** y)
from itertools import count
from pydoc import apropos

# Even Or Odd
# x = int(input("Enter The Number : "))
# if x%2 == 0:
#     print(x, " is an even number")
# else:
#     print(x, " is an odd number")

#Largest Three
# x = int(input("Enter The Number : "))
# y = int(input("Enter The Number : "))
# z = int(input("Enter The Number : "))
# print(max(x, y, z))

# Fizz Or Buzz
# for i in range(1, 101):
#     if i%3 == 0: print(i, " Fizz")
#     elif i%5 == 0: print(i, " Buzz")
#     elif i%3==0 and i%5==0: print(i, " FizzBuzz")

# Sum of the list
# ar = [1,2,3,4,5,6]
# print(sum(ar))

# Avg Of The list
# ar = [1,2,3,4,5,6]
# print(sum(ar)/ len(ar))

# Max Of The List
# ar = [1,2,3,4,5,6]
# print(max(ar), min(ar))

#Swap Two Numbers
# def swap(a, b):
#     return b,a
# x = 10
# y = 20
# # x,y = y,x
# x,y = swap(x,y)
# print(x, y)

# Count Word & store occurrence in dict
# st = "hello World hello World "
# word = st.split()
# dic = {}
# for i in word:
#     if i in dic:
#         dic[i] +=1
#     else:
#         dic[i] = 1
# print(dic)

# Merge two dict
# dic1 = {
#     "name ": "hello"
# }
# dic2 = {
#     "hel ": "aftab"
# }
# res = {**dic1, ** dic2}
# print(res)

# Anagram Or Not
# s = input("Enter 1st St : ")
# t = input("Enter 2nd St : ")
# if sorted(s) == sorted(t):
#     print("Anagram")
# else:
#     print("Not Anagram")

# st = "Hello World!"
# count = 0
# for i in st:
#     count +=1
# print(count)