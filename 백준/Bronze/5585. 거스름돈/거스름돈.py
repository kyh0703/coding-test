N = int(input())
money = 1000 - N
answer = 0
while True:
    if money <= 0:
        break
        
    for i in (500, 100, 50, 10, 5, 1):
        while money // i:
            money -= i
            answer += 1

print(answer)
