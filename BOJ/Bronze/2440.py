n =  int(input())

## 풀이 1
for i in range(n) :
    for j in range(n - i) :
        print("*", end="")
    print()
    
    
## 더 나은 풀이2
for i in range(n) :
    print("*" * (n - i))