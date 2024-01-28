# Silver

import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().strip().split()))
A.sort()

for i in check :
    low = 0
    high = n - 1
    flag = 0
    while (low <= high) :
        mid = (low + high)//2
        if i < A[mid] :
            high = mid - 1
        elif i > A[mid] :
            low = mid + 1
        else :
            flag = 1
            break
    print(flag)