n = int(input())
count = 0
for _ in range(n):
    word = input()
    alphabet = [0] * 26
    flag = 1

    for i in range(len(word)):
        if alphabet[ord(word[i]) - 97] == 0:
            alphabet[ord(word[i]) - 97] = 1
        elif word[i] != word[i - 1]:
            flag = 0
            break
    if flag:
        count += 1
print(count)