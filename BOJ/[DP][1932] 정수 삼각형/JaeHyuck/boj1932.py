import sys
input = sys.stdin.readline

num= int(input())
dp = [] # 삼각형
for i in range(num):
    dp.append(list(map(int, input().split())))

dp1= [] + dp #memoization용


for i in range(num-1,0,-1):
    for j in range(len(dp[i-1])):
        dp1[i-1][j]=dp[i-1][j]+max(dp[i][j],dp[i][j+1])

print(dp1[0][0])
