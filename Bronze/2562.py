list_num = []
for i in range(9) :
    n = int(input())
    list_num.append(n)

temp = 0
temp_index = 0
for i in range(9) :
    if list_num[i] > temp :
        temp_index = i
        temp = list_num[i]

print(temp)
print(temp_index + 1)