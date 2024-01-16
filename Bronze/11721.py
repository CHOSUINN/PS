# 정답 1
sentence = [x for x in input()]
for i in range(len(sentence)) :
    print(sentence[i], end="")
    if (i + 1) % 10 == 0:
        print()
        
# 효율성을 높히기 위해 슬라이싱을 활요한 정답 2        
sentence = input()
print_size = 10
for i in range(0, len(sentence), print_size):
    print(sentence[i: i + print_size])