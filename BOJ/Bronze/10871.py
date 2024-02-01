n, x = map(int, input().split())

list_num = list(map(int, input().split()))

for i in range(n) :
    if (list_num[i] < x) :
        print(list_num[i], end = " ")