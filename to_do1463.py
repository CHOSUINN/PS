# Silver

n = int(input())
count = 0
while (n % 3 == 0 or n % 2 == 0) and n > 1 :
    if n % 3 == 0 :
        n //= 3
        count += 1
    elif n % 2 == 0 :
        n //= 2
        count += 1
    else :
        n -= 1
        count += 1
print(count)
        
        