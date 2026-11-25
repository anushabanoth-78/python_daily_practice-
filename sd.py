import copy
a = [10, [20, 30], 40]
b = copy.copy(a)
c = copy.deepcopy(a)
b[1][0] = 200
c[1][1] = 300
print(a)
print(b)
print(c)
