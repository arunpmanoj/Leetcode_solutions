# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):

        if k == 0 or head is None:
            return head
        length = 1
        curr = head
        while curr.next is not None:
            length +=1
            curr = curr.next
        k=k%length
        if k == 0:
            return head
        curr.next = head
        curr = head
        for i in range (1,length-k):
            curr = curr.next 
        head = curr.next
        curr.next = None
        return head
            