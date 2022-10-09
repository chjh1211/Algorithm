import sys
N = int(sys.stdin.readline())
n = N//5
for i in range(n,-1,-1):
    count = i
    a = N - 5*i
    if(a%3 == 0):
        count+=a//3
        break
    if(i == 0 and a%3!=0):
        count = -1

print(count)
