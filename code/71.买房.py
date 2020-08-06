t = int(input())
for i in range(t):
    A = list(map(int, input().split()))
    n,k = A[0],A[1]
    if n <= 2 or k >= n or  k < 2:
        print(0,0)
    else:
        maxnum = min(n-k,k-1) # n 为偶数的情况下，最大的是k-1,n为奇数的情况下，最大的是n-k
        print(0,maxnum)