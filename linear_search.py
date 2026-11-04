#Find 30 in [10, 20, 30, 40, 50] using Linear Search. Return its index.
def Linear_Search(arr,target):
    for i in range(1,6):
        if arr[i] ==target:
            return i
    return -1
    
arr =[10, 20, 30, 40, 50]
target=30
print("element in the index of:",Linear_Search(arr,target))