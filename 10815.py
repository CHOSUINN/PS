# Silver

# 풀이1 
# 파이썬의 딕셔너리는 속도가 빠른편이라 딕셔너리로 풀수 있다.
import sys

n = int(sys.stdin.readline().strip())
list1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
list2 = list(map(int, sys.stdin.readline().strip().split()))

_dict = {}
for i in range(n) :
    _dict[list1[i]] = 1
    
for i in range(m) :
    if list2[i] in _dict :
        print(1, end=" ")
    else :
        print(0, end=" ")
        
        
# 풀이 2
# 문제의 의도대로 이진탐색을 활용하여 문제를 풀어보자
# 이진 탐색 방법

n = int(sys.stdin.readline().strip())
list1 = sorted(list(map(int, sys.stdin.readline().strip().split())))
m = int(sys.stdin.readline().strip())
list2 = list(map(int, sys.stdin.readline().strip().split()))

for i in range(m) :
    low = 0
    high = n - 1
    flag = 0
    while low <= high :
        mid = (low + high) // 2
        if list2[i] > list1[mid] :
            low = mid + 1
        elif list2[i] < list1[mid] :
            high = mid - 1
        else :
            flag = 1
            break
    print(flag, end =" ")