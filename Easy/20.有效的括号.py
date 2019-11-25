#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        while len(s) != 0:
            s = s.replace("()", "", 1)
            s = s.replace("[]", "", 1)
            s = s.replace("{}", "", 1)
            if (s.find("()") == -1) and (s.find("[]") == -1) and (s.find("{}") == -1):
                if len(s) != 0:
                    return False
                break
        return True
            

print(Solution().isValid("()[]{}"))
# @lc code=end

