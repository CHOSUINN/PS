# Bronze
import sys

t = int(sys.stdin.readline().strip())

for _ in range(t) :
    floor = int(sys.stdin.readline().strip())
    room_num = int(sys.stdin.readline().strip())

    room = [[0]*room_num for _ in range(floor + 1)]
    for i in range(room_num) :
        room[0][i] = i + 1
        
    for i in range(1, floor + 1) :
        for j in range(room_num) :
            if j == 0 :
                room[i][j] = 1
            else :
                room[i][j] = room[i][j - 1] + room[i - 1][j]
    print(room[floor][room_num - 1])


# 제한 값이 14라는 점에서 O(n^2)으로 풀수 있을거라 생각하여 완전 탐색으로 풀이했다.
# 하지만 반대로 입력값이 14라는 점을 생각해서 미리 14*14배열을 만들어 dp로 문제 풀이를 할 수도 있다.