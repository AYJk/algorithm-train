#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return head
        tmp = head.val
        current = head
        while current.next != None:
            if tmp == current.next.val:
                current.next = current.next.next
                continue
            current = current.next
            tmp = current.val
        return head
# @lc code=end

