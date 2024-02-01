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
# 초기화: 탐색을 시작하기 위해, 'low'(최소 인덱스)와 'high'(최대 인덱스)라는 두 포인터를 정의합니다. 처음에는 'low'를 배열의 첫 번째 인덱스로, 'high'를 배열의 마지막 인덱스로 설정합니다.

# 중간 값 찾기: 배열의 중간 지점을 찾습니다. 중간 지점 'mid'는 'low'와 'high'의 평균으로 계산됩니다. 대부분의 경우, 'mid = (low + high) / 2'로 계산합니다.

# 비교: 배열의 'mid' 위치에 있는 값을 찾고자 하는 값과 비교합니다. 세 가지 경우가 있습니다:

# 찾고자 하는 값이 'mid' 위치의 값과 같다면, 원하는 값을 찾은 것이므로 탐색을 종료합니다.
# 찾고자 하는 값이 'mid' 위치의 값보다 작다면, 'high'를 'mid - 1'로 업데이트하여 탐색 범위를 하반부로 줄입니다.
# 찾고자 하는 값이 'mid' 위치의 값보다 크다면, 'low'를 'mid + 1'로 업데이트하여 탐색 범위를 상반부로 늘립니다.
# 반복 또는 종료: 위 단계를 반복하며 값을 찾습니다. 만약 'low'가 'high'를 초과하는 순간이 오면, 배열 안에 찾고자 하는 값이 없다는 것을 의미하며 탐색을 종료합니다.

# 이진 탐색은 다음과 같은 특징을 가지고 있습니다:

# 정렬된 배열 필요: 이진 탐색은 정렬된 배열에서만 효과적으로 작동합니다.
# 분할 정복 알고리즘: 이진 탐색은 분할 정복 방법론을 사용하는 대표적인 예입니다.
# 효율적인 탐색: 대규모 데이터셋에서도 빠르게 탐색할 수 있어 효율적입니다.
# 반복 또는 재귀적 구현 가능: 이진 탐색은 반복문 또는 재귀 함수를 사용하여 구현할 수 있습니다.

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