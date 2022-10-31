N = int(input())

list =[]
cnt=1

for i in range(N):
    a, b = map(int, input().split())
    list.append([a,b])


list.sort(key=lambda x:x[0])
list.sort(key=lambda x:x[1])

cmp = list[0][1]

for j in range(1,N):
    if list[j][0] >= cmp:
        cnt+=1
        cmp = list[j][1]

print(cnt)