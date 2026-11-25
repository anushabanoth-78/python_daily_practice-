import copy
a = [10, [20, 30], [40, 50]]
b =copy.deepcopy(a)
b[1][0] =200
b[2][1] = 500
print(a)
print(b)
