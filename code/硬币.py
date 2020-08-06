class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins = [7,2,3,6]
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i],n+1):
                dp[j] += dp[j-coins[i]]
                print("DP:",dp)

        return dp[-1] % 1000000007

# print(Solution().waysToChange(7))

# 连续的子数组和
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a = sum(nums[i:j])
                if a == k  or (k!=0 and a % k == 0 ):
                    return True
        return False


# print(Solution().checkSubarraySum([0,0],0))


# 和为k的子数组
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
class Solution:
    def subarraySum(self, nums,k: int) -> int:
        pre = 0
        count = 0
        dic = {0:1}
        for i in nums:
            pre += i
            print("pre:",pre)
            if (pre-k) in dic:
                print("pre-k",pre-k)
                count += dic[pre-k]
            dic[pre] = dic.get(pre,0) + 1
            print("dic:",dic)
        return count

# print(Solution().subarraySum([2,3,2,5,1],7))


# 最大子数组之和
def maxnums(num):
    dp = [0]*len(num)
    dp[0] = num[0]

    for i in range(1,len(num)):
        dp[i] = max(num[i],dp[i-1]+num[i])
        # print(dp[i-1]+dp[i])
    print(dp)
    return max(dp)

    # 方法二
    # maxnum = nums[0]
    # sum = 0
    # for i in nums:
    #     if sum > 0:
    #         sum += i
    #     else:
    #         sum = i
    #     maxnum = max(sum,maxnum)
    # return maxnum


    """
    for i in range(1,len(nums)):
        nums[i] = nums[i] + max(nums[i-1],0)
    return max(nums)
    """

print(maxnums([12,-4,32,-36,12,6,-6]))


# 汽车加油
def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    rest = 0
    minvalue = 0
    index = 0

    for i in range(len(gas)):
        rest += gas[i] - cost[i]
        if rest < minvalue:    # 小于零的时候需要重新计数。
            minvalue = rest
            index = i + 1  # 记录当前加油站位置
    if rest < 0:
        return -1
    else:
        return index

# 贪心策略，线性遍历
def canCompleteCircuit(self, gas, cost):
    total_tank = 0
    cur_tank = 0
    index = 0
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        cur_tank += gas[i] - cost[i]   # 当cur小于零的时候，代表前半程的汽油不够，所以需要从该站的下一站重新出发！
        if cur_tank < 0:
            cur_tank = 0
            index = i + 1
    return index if total_tank >= 0 else -1