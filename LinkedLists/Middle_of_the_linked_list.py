# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        curr = head
        count = 0
        temp =head 
        while temp  :
            count += 1
            temp=temp.next 
        mid =count // 2

        for _ in range(mid):
            curr=curr.next
        return curr
