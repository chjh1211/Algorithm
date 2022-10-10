import sys
N,K = map(int,sys.stdin.readline().split())
A =[]
count = 0
n=K
for i in range(N):
    A.append(int(sys.stdin.readline()))

for i in range(N-1,-1,-1):
    count += n//A[i]
    n%=A[i]

print(count)