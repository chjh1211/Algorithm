n = int(input())

count = n // 2
dp = [0] * 1001

def factorial(a):
    temp= 1 
    if a!= 0:
        for i in range(a,0,-1):
            temp *= i
    dp[a] = temp
    return dp[a]

def combi(a,b):

    if dp[a] != 0: a1 = dp[a]
    else: a1 = factorial(a)

    if dp[b] != 0: b1 = dp[b]
    else: b1 = factorial(b)

    if dp[a-b] != 0: c1 = dp[a-b]
    else: c1 = factorial(a-b)
    
    return a1//(b1*c1)

result = 0

for i in range(count,-1,-1):
    result += combi(n-i,i)

print(int(result%10007))
    
    
