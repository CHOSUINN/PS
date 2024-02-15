# Silver

from sys import stdin

n = int(stdin.readline().rstrip())

total = 0
for i in range(1, n + 1) :
    total += (n//i) * i
print(total)