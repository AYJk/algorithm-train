#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while slow != None:
            if fast == None:
                return slow
            elif fast.next == None:
                return slow.next
            slow = slow.next
            fast = fast.next.next

# @lc code=end

