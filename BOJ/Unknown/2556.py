## 풀이1 오답!
import time
n = int(input())

for i in range(n) :
    print("*")
    time.sleep(5)
    

## 풀이 2 정답!

n = int(input())

for i in range(n) :
    print("*" * n)