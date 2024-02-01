# Silver
# 문자열의 길이를 세서 그 길이를 담은 리스트 strlen. 답을 담고 있는 answer리스트. 
# 입력값을 받아서 strlen리스트에서 길이를 비교 만약 str보다 길이가 긴 게 있으면 그 앞에자리 insert.
# 만약 값이 같으면 같은 값 바로 뒤 자리에 insert

import sys

n = int(sys.stdin.readline())
answer = set()

for _ in range(n):
    answer.add(sys.stdin.readline().strip())

answer = list(answer)
answer.sort()
answer.sort(key=len)
for word in answer :
    print(word)
    

# 풀이 2 : same algroithm but got time abort. 
import sys

n = int(sys.stdin.readline())
answer = list(set(sys.stdin.readline().strip() for _ in range(n)))

for i in range(len(answer)) :
    min_index = i
    for j in range(i + 1, len(answer)) :
        if len(answer[j]) < len(answer[min_index]) or (len(answer[j]) == len(answer[min_index]) and answer[j] < answer[min_index]):
            min_index = j
    answer[i], answer[min_index] = answer[min_index], answer[i]
    
for word in answer :
    print(word)