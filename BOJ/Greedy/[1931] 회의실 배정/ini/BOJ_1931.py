import sys
N = int(sys.stdin.readline())
M = [] # 회의 시작 & 종료 시간
ans =1 # 회의 갯수
for i in range(N):
    M.append([int (x) for x in sys.stdin.readline().split()])

M.sort(key=lambda x : (x[1],x[0])) # 회의 시간 정렬
n = M[0][1] 

for i in range(1,N):
    if(M[i][0] >= n):
        ans+=1
        n = M[i][1]

print(ans)
