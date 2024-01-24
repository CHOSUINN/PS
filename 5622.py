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

# 풀이 2
dial_dict = {"ABC" : 3, "DEF" : 4, "GHI":5, "JKL" : 6, "MNO" : 7, "PQRS" : 8, "TUV" : 9, "WXYZ" : 10}

input_str = sys.stdin.readline().strip()
answer =  0
for i in input_str :
    for key, val in dial_dict.items() :
        if i in key :
            answer += val
print(answer)