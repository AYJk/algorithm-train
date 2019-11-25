#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ans = strs[0]
        for index in range(1, len(strs)):
            for anIndex in range(0, len(ans)):
                subLength = len(strs[index]) - 1
                if anIndex <= subLength:
                    if ans[anIndex] != strs[index][anIndex]:
                        ans = ans[:anIndex]
                        break
                else:
                    ans = ans[:subLength + 1]
                    break
        return ans

print(Solution().longestCommonPrefix(["dog","racecar","car"]))
# @lc code=end