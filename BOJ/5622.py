# Bronze
# 풀이 1
import sys

input_str = sys.stdin.readline().strip()
time_count = 0
base_time = 2
for i in input_str :
    calculate_time = ord(i) - 65 + 1
    if calculate_time <= 15 :
        if calculate_time % 3 == 0 :
            time_count += calculate_time//3
        else : 
            time_count += calculate_time//3 + 1
    elif 15 < calculate_time < 20 :
        time_count += 6
    elif 19 < calculate_time < 23 :
        time_count += 7
    else :
        time_count += 8
print(time_count + len(input_str)*base_time)

# sys.stdin.readline().strip()에 strip을 안붙혀서 자꾸 결과가 음수로 나왔다. 그 원인을 한참 못찾았네. strip()을 해주지 않으면 개행(\n)이 같이 문자열에 포함된다는걸 잊지말자
# 딕셔너리를 활용해서 풀까도 생각했는데 {"A" : 1, "B":2..."Z" : 26}하는게 너무 하드 코딩같아서 안했는데 다른 풀이 방법 보니까 리스트에 ["ABC","DEF"...,"WXYZ"]등으로 넣어 활용하고 인덱스 값을 더하는 식으로 했더라.. 묶어서 넣어서 활용할 수 있다는걸 잊지말자

# 풀이 2
dial_dict = {"ABC" : 3, "DEF" : 4, "GHI":5, "JKL" : 6, "MNO" : 7, "PQRS" : 8, "TUV" : 9, "WXYZ" : 10}

input_str = sys.stdin.readline().strip()
answer =  0
for i in input_str :
    for key, val in dial_dict.items() :
        if i in key :
            answer += val
print(answer)