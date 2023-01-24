n = int(input())

array = [0]*(n*n+1)

for i in range(1,n+1):
    temp = list(map(int, input().split()))
    for j in range(1,i+1):
        array[j+(n*(i-1))] = temp[j-1]


for j in range(((n-1)*(n-1)+(n-2)),0,-1):
        array[j] = array[j] + max(array[j+n],array[j+n+1])

print(array[1])
