def badFibo(N):
	if N<=1:
		return N
	else:
		return badFibo(N-1)+badFibo(N-2)



def fibMemory(n,dp):
	if dp[n]!=-1:
		return dp[n]
	if n<=1:
		dp[n]=n
		return dp[n]
	dp[n]=fibMemory(n-1,dp)+fibMemory(n-2,dp)
	return dp[n]

#x=badFibo(40)
#print("Fibo de 40=",x)


def fibBottomUp(n):
	if n<=1:
		return n

	dp=[0]*(n+1)
	dp[1]=1
	for i in range(2,n+1):
		dp[i]=dp[i-1]+dp[i-2]

	return dp[n]


n=100
dp=[-1]*(n+1)
print("Mem Fibo de 100=",fibMemory(n,dp))
print("Bottom up Fibo de 100=",fibBottomUp(n))


#x=badFibo(40)
#print("Fibo de 40=",x)