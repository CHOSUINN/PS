## time out..

def d(n) :
    sum = n
    while n != 0 :
        sum += n % 10
        n //= 10
    return sum

def findSelfNumber(num) :
    array = []
    for i in range(1, num) :
        array.append(d(i))
    for i in array :
        if num == i :
            return 1
    return 0

for i in range(1, 10001) :
    if findSelfNumber(i) == 0 :
        print(i)


## wah-lah

def d(n) :
    sum = n
    while n > 0 :
        sum += n % 10
        n //= 10
    return sum

generated_numbers = set()
for i in range(1, 10001):
    generated_numbers.add(d(i))

for i in range(1, 10001):
    if i not in generated_numbers:
        print(i)