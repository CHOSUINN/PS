# Silver
                
    
m, n = map(int,input().split())

num = [0] * (n + 1)

for i in range(2, n + 1) :
    if num[i] == 0 :
        if i >= m :
            print(i)
        for j in range(i, n + 1, i) :
            num[j] = 1