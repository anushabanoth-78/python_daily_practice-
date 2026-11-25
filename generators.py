# Write a Python generator function called count_numbers(n) that generates
#  numbers from 1 to n using yield.

def count_numbers(n):
    for num in range(1, n + 1):
        yield num


for num in count_numbers(5):
    print(num)
