def bag(n, c, w, v):
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j < w[i - 1]:
                value[i][j] = value[i - 1][j]
            else:
                value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])
        # 背包总容量够放当前物体，取最大价值
    return value


def bag1(N, V, w, v):
    dp = [0 for i in range(V + 1)]  # 背包容量对应的价值大小
    for i in range(N):  # 循环N个物品
        for j in range(V, v[i] - 1, -1):  # # 从容量开始往下递减

            dp[j] = max(dp[j], dp[j - v[i]] + w[i])

    return dp[-1]


#
# print(bag(6,10, [2, 2, 3, 1, 5, 2],[2, 3, 1, 5, 4, 3]))
# print(bag1(6,10, [2, 3, 1, 5, 4, 3],[2, 2, 3, 1, 5, 2]))

class Solution:
    # 这里的代码和01背包问题代码一样，只是在输入时，对数组v,w和物品件数n进行了调整
    def max_value(self, n, m, v, w):
        dp = [0] * (m + 1)
        for i in range(n + 1):
            for j in range(m, v[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])
        return dp[m]


if __name__ == '__main__':

    A = list(map(int,input().split()))
    n,m = A[0],A[1]

    v = [0]
    w = [0]
    c = 0
    for i in range(n):
        line = list(map(int, input().split()))
        v.extend([line[0]] * line[2])
        w.extend([line[1]] * line[2])
        c += line[2]
    print(Solution().max_value(c, m, v, w))

