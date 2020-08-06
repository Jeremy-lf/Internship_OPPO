
# d堆排序
def max_heapify(ary,start,end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:  # 判断是否存在子节点
            break
        if child + 1 <= end and  ary[child] < ary[child + 1]:  # 存在右节点，并且有节点小于左节点
            child = child + 1

        if ary[root] < ary[child]: # 根节点小于左节点
            ary[root],ary[child] = ary[child],ary[root]   # 较大的子节点成为父节点
            root = child
        else:
            break

    return ary


def heap_sort(ary):
    n = len(ary)
    first = int(n/2) -1
    for start in range(first,-1,-1):  # 循环每个父节点，构建大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)  # 堆排，将大根堆转换成有序数组
    return ary


# 最长上升子序列

def longestsubsequence(nums):
    dp = [1 for i in range(len(nums))]

    res = 0
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i],dp[j]+1)
        res = max(dp[i],res)
    return res

# 冒泡排序

def bubblesort(nums):
    for j in range(len(nums)-1):
        for i in range(len(nums)-1-j):
            if nums[i] > nums[i+1]:
                nums[i+1],nums[i] = nums[i],nums[i+1]
    return nums

# 选择排序

def select_sort(nums):
    for i in range(len(nums)):
        minindex = i

        for j in range(i+1,len(nums)):
            if nums[j] < nums[minindex]:
                minindex = j
        nums[minindex],nums[i] = nums[i],nums[minindex]
    return nums