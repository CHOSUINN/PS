## 문제 풀이 1 정답이긴 하지만 너무 시간이 오래걸리고 코드 효율이 떨어져 보인다
def multiples_of_3(n) :
    if n % 3 == 0 :
        answer.append(n//3)
        
def multiples_of_5(n) :
    if n % 5 == 0 :
        answer.append(n//5)

n = int(input())
answer = []
count = 0

multiples_of_3(n)
multiples_of_5(n)
while n >= 5 :
    n -= 5
    count += 1
    if n % 3 == 0 :
        temp = count
        temp += n//3
        answer.append(temp)
answer.sort()
if len(answer) == 0 :
    print(-1)
else :
    print(answer[0])


## 문제 풀이2
n = int(input())
bag = 0

while n >= 0 :
    if n % 5 == 0 :
        bag += n//5
        print(bag)
        break
    n -= 3         # 3kg를 빼는 이유는 5kg가방을 최대한 많이 써야 가방의 갯수를 줄일 수 있기 때문
    bag += 1

if n < 0 :
    print(-1)