#Write a Python program to create a shallow copy of this nested list
import copy


a = [10, [20, 30], 40]
b = copy.copy(a)
b[0] =200
print(a)
print(b)

