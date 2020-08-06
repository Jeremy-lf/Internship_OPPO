A = list(map(int, input().split()))
n,m = A[0],A[1]

B = {}
for i in range(n):
    C = list(map(int, input().split()))
    x,y = C[0],C[1]
    if x in B:
        B[x].append(y)
    else:
        B[x] = [y]

# 统计票数最高的
ticket = 0
for i in B.keys():
    if len(B[i]) > ticket:
        ticket = len(B[i])

# 大神的票数
if 1 in B.keys():
    vote = len(B[1])
    del B[1]
else:
    vote = 0


for k in range(ticket+1,0,-1):
    num = 0
    # for i in B.keys():
    #     while len(B[i]) >= k:

candy_all=[] #初始化糖果数存放列表
# 两步操作
for k in range(candi_max+1,0,-1):
    candy=0
    for i in d.keys():
        while(len(d[i])>=k):
            candy=candy+min(d[i])
            d[i].remove(min(d[i]))
            vote=vote+1
    if vote<k:
        li=[]
        for j in d.keys():
            li.append(d[j])
        li = sum(li,[]) #二维列表压缩成一维
        li.sort() #默认为升序
        if len(li)>0:
            for p in range(0,k-vote):
                candy=candy+li[p]
    candy_all.append(candy)
print(min(candy_all))