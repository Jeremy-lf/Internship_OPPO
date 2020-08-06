import math
'''
小明很喜欢数对，又很喜欢GCD(最大公约数)。所以他想尽办法创造了一种全新的最大公约数：
给出若干个数对(ai,bi)，如果一个最大的质数x可以整除每一个数对中的至少一个数字并且这个数字大于1，那么x就称为这些数对的N-GCD。
现在小明给了你一些数对，希望你可以算出它们的N-GCD。
'''
'''
在读取数字的时候顺便计算下最小值min，之后找出[2,min]之间的素数，并从大到小遍历，判断该数能否整除除nums数组中每一个数对中的任意一个值。
'''

n = int(input())
B = []
min_val = 1e9
for i in range(n):
    A = list(map(int,input().split()))
    B.append(A)
    min_val = min(min_val,A[0],A[1])

# 判断是否为素数
def Isprieme(n):
    if n <= 2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


# 判断能否被整除
def divsion(n):
    for num in B:
        if num[0] % n != 0 and num[1] % n != 0:
            return False
    return True


# 遍历求出2-min_val间的最小值

prime = []
for i in range(min_val,1,-1):
    if Isprieme(i):
        prime.append(i)
print("prime:",prime)

# 遍历所有的数组，如果不能整除，则不记录
res = 1e9
for val in prime:
    sat = True
    for i in range(n):
        if B[i][0] % val != 0 and B[i][1] % val != 0:
            sat = False
            break
    if sat:
        res = val
        break

print(res) if res != 1e9 else print(-1)