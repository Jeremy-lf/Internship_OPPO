'''
题目给定a1,a2...an，这样一个长度为n的序列，现在你可以给其中一些元素加上一个值x（只能加一次），
然后可以给另外一些值减上一个值x（只能减一次），剩下的元素不能再进行操作。问最后有没有可能找到一个值x使所有元素的值相等。
'''
'''
1
5
1 3 3 2 1
'''

k = int(input())

for i in range(k):
    n = int(input())
    A = list(map(int,input().split()))

    A = list(set(A))
    A.sort()

    if len(A) < 3:
        print("YES")
    elif len(A) == 3 and A[2]-A[1] == A[1]-A[0]:

        print("YES")
    else:
        print("NO")
