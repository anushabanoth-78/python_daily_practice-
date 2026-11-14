def fibnaci(n):
     if n==0:
          return 0
     if n==1:
          return 1
     return fibnaci(n-1)+fibnaci(n-2)

print(fibnaci(10))