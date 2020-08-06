class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if N==1:return 1
        dp = [1] * K
        ans = 2
        while True:
            for i in range(K-1,0,-1):
                dp[i] = dp[i]+dp[i-1]+1
            dp[0] = ans
            if dp[-1]>=N:
                return ans
            ans+=1


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dpTable = [[0] * (N + 1) for _ in range(K + 1)]
        m = 0
        while (dpTable[K][m] < N):
            m += 1
            for k in range(1, K + 1):
                dpTable[k][m] = dpTable[k - 1][m - 1] + dpTable[k][m - 1] + 1

        return m




'''
牛牛和妞妞在一天晚上决定一起去看一场情人节演唱会，可是由于这场演唱会实在太出名了，有很多情侣都来观看，牛牛和妞妞不小心被人流冲散了！
维持秩序的人决定，让大家排成一列，相邻两个进去的人（2k-1和2k，k为正整数）坐在相邻座位。但是现在的队伍乱糟糟的，有很多情侣都不在相邻位置。维持秩序的人同意让情侣们跟相邻的人交换位置，直到所有情侣都在2k-1和2k位置上为止。
但是维持秩序的人很没有耐心，所以需要最少的交换次数，你能帮情侣们算出这个次数吗？
'''
'''

n = int(input())
A = list(map(int,input().split()))
count = 0
while len(A) > 0:
    first = A[0]  # 记录第一个元素
    A.pop(0)  # 弹出第一个元素
    index = A.index(first)
    count += index
    del A[index]   # 删除这一对已经匹配的元素

print(count)
'''

from math import ceil

n = int(input())


# 定义一个函数，计算不同的m,当分完贝壳的时候，妞妞的贝壳数量
def check_num(n, m):
    x1, x2 = 0, 0
    while n > 0:
        t1 = m if m <= n else n
        n -= t1
        x1 += t1

        t2 = n // 10
        n -= t2
        x2 += t2
    return x1


left = 1
right = n
while left <= right:
    mid = left + (right - left) // 2
    x1 = check_num(n, mid)

    if x1 < ceil(n / 2):
        left = mid + 1
    else:
        right = mid - 1
print(left)