# Bronze

import sys

s = sys.stdin.readline().strip()
alphabet = [0] * 27
for i in s :
    alphabet[ord(i) - 97] += 1

for i in range(26) :
    print(alphabet[i], end=" ")