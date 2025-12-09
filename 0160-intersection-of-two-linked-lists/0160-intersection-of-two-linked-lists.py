# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None
        monk1,monk2 = headA,headB
        while monk1 !=monk2:
            if monk1:
                monk1=monk1.next
            else:
                monk1=headB
            if monk2:
                monk2=monk2.next
            else:
                monk2=headA
        return monk1