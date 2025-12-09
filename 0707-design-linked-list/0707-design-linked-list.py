class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >=self.size:
            return -1
        monk=self.head
        for _ in range(index):
            monk=monk.next
        return monk.data

    def addAtHead(self, val: int) -> None:
        tmp=Node(val)
        tmp.next = self.head
        self.head=tmp
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        tmp=Node(val)
        if self.size==0:
            self.head=tmp
        else:
            monk=self.head
            while monk.next:
                monk=monk.next
            monk.next=tmp
        self.size +=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index ==0:
            self.addAtHead(val)
            return 
        if index == self.size:
            self.addAtTail(val)
            return
        tmp=Node(val)
        monk=self.head
        for i in range(index-1):
            monk=monk.next
        tmp.next=monk.next
        monk.next=tmp
        self.size +=1
        
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index>=self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            monk=self.head
            for i in range(index-1):
                monk=monk.next
            monk.next=monk.next.next
        self.size -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)