#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        current = pre
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
                continue
            current = current.next
        return pre.next
# @lc code=end

