n = int(input())
time = list(map(int, input().split()))
time.sort()

sum = 0
addList = []

for i in range(n):
    sum += time[i]
    addList.append(sum)

sum = 0
for num in addList:
    sum += num
print(sum) 