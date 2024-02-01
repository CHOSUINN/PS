n = int(input())
list_num = list(map(int, input().split()))

min_num = 1000000
max_num = -1000000
for i in range(n) :
    if (list_num[i] > max_num) :
        max_num = list_num[i]
    if (list_num[i] < min_num) :
        min_num = list_num[i]
print(min_num, max_num)