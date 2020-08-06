class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = min(len(i) for i in strs)
        k = 0
        tmp = strs[0]
        for i in range(min_len):
            for j in range(1, len(strs)):
                if tmp[i] != strs[j][i]:
                    # return ""
                    break
            k += 1
        return tmp[k]
print(Solution().longestCommonPrefix(["flower","flow","flight"]))


def aa(strs):
    minlen = min([len(x) for x in strs])
    k = 0
    tmp = strs[0]
    for i in range(minlen):
        for j in range(len(1,strs)):
            if tmp[i] != strs[j][i]:
                break
        k += 1
    return tmp[k]
            