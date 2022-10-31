N, K = map(int, input().split())
cnt = 0
list = []

for i in range(N):
    list.append(int(input()))
list.sort(reverse=True)

for m in list:
    if K >= m:
        cnt += K//m
        K = K%m
    if K==0: break

print(cnt)

