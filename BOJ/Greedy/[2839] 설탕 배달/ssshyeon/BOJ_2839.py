num = int(input())

cnt = 0
if num >= 5:
    cnt += num // 5
    num = num % 5

while (num%3 != 0 and cnt >= 0):
    cnt -=1
    num +=5

if cnt >= 0:
    cnt += num//3
    print(cnt)
else:
    print(-1)
