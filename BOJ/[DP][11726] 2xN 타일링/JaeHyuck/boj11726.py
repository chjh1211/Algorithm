import sys
input = sys.stdin.readline

num= int(input())

dp =[0]*100000
dp[1]=1
dp[2]=2
dp[3]=3
for i in range(4,num+1):
    dp[i]= dp[i-2]+dp[i-1]
print(dp[num])
