# Silver

import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n) :
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in answer :
    print(i)