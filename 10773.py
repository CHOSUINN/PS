k = int(input())
money_record = []
for _ in range(k) :
    price = int(input())
    if price :
        money_record.append(price)
    else :
        money_record.pop()
print(sum(money_record))