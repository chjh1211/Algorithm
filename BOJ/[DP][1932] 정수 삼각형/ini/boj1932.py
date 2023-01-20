import sys
n = int(sys.stdin.readline())
arr, dp = [], []

for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().split()])
    dp.append([0 for _ in range(i+1)])
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0 : 
            dp[i][j] = arr[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[n-1]))

