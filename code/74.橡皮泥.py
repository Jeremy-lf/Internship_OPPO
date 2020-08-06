'''

一天小易得到了一串橡皮泥，这串橡皮泥只有黑色和白色，小易想把这串橡皮泥重新拼凑一下，让这个橡皮泥串中最长的连续的黑白相间的子串最长，但是小易有强迫症，所以他可以对橡皮泥串进行以下的操作0次或多次：
把橡皮泥串从某个地方切割开，将两个得到的两个串同时翻转，再拼接在一起。
这个橡皮泥串可能太长了，所以小易没有办法计算最终可以得到的最长的连续的黑白相间的子串的长度，希望你能帮他计算出这个长度。
'''

'''
//根据反转前后相对位置不变，相当于在一个环上找最长子串
'''
s = input()
s += s
res = 0
for i in range(len(s)):
    j = 1
    while i < len(s)-1 and s[i] != s[i+1]:
        j += 1
        i += 1
    if j > res:
        res = j
if res > len(s)/2:
    res = len(s)/2
print(res)


# maxnum = 0
# t = 1
# s += s[0]
# for i in range(len(s)):
#     if s[i] != s[i+1]:
#         t += 1
#     else:
#         if t > maxnum:
#             maxnum = t
#         t = 1
# if t > maxnum:
#     maxnum = t
# print(maxnum)