#!/bin/python3



# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = sum([n for n in arr])
    print(total-(max(arr)), total-min(arr))



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)
