'''

给你n张卡片，卡片上仅包含大写英文字母，现你可从这n张卡片中选出k张，要求得到尽可能高的分数。
关于分数的计算方式，在你所选择的k张卡片中，含有相同字母的卡片分数为卡片数乘以相同卡片个数。
就样例而言，选择九张D和其他任意一张，得到的结果为9*9+1 。

15 10
DZFDFZDFDDDDDDF
'''

A = list(map(int,input().split()))
n, k = A[0], A[1]
S = input()


# 统计每个字母的卡片个数
res = {}
for i in S:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
values = list(res.values())
values.sort(reverse=True)
count = 0


for v in values:
    if k >= v:
        count += v*v
        k -= v
    else:
        count += k**2  # 剩下几个就选几个
        break
print(count)


