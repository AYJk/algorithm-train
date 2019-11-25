#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        spcList = ["IV", "IX", "XL", "XC", "CD", "CM"]
        total = 0
        for spcStr in spcList:
            if spcStr in s:
                total += dic[spcStr]
                s = s.replace(spcStr, "")
        for leftNum in s:
            total += dic[leftNum]
        return total

