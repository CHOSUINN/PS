n = int(input())
for _ in range(n) :
    answer = 0
    temp = input()
    for i in temp :
        if i == "(" :
            answer += 1
        elif i == ")" :
            if answer == 0 :
                answer -= 1
                break
            answer -= 1
    if answer == 0 :
        print("YES")
    else :
        print("NO")