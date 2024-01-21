# Silver

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