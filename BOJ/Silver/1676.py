#Silver
# 풀이 1
def factorial(num) :
    val = 1
    if num == 0 or num == 1 :
        return 1
    else :
        for i in range(2, num + 1) :
            val *= i
        return val

n = int(input())
count = 0
num = factorial(n)
num = [x for x in str(num)]
for i in range(len(num) - 1, -1, -1):
    if num[i] == '0' :
        count += 1
    elif num[i] != '0' :
        break
print(count)


# 더 좋은 풀이 2
def number_of_zero(n) :
    count = 0
    i = 5
    while(n/i >= 1) :
        count += int(n / i)
        i *= 5
    return count

n = int(input())
print(number_of_zero(n))