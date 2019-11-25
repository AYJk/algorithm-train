#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:    
            temp = 0
            while x != 0:
                y = x % 10
                if y == 0 and temp == 0:
                    return False
                temp = temp * 10 + y
                x //= 10
                if temp > x and temp // 10 == x or temp == x:
                    return True
        return False
            
print(Solution().isPalindrome(11))
 