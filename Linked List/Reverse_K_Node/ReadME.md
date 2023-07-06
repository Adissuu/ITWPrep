# Reverse k list

### Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

### k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

### You may not alter the values in the list's nodes, only nodes themselves may be changed.


```
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        prevGr = dummy
        
        
        while True:
            kth = self.getKthNode(prevGr, k)
            if not kth:
                break
            nextGr = kth.next

            prev, current = nextGr, prevGr.next
            while current != nextGr:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            temp = prevGr.next
            prevGr.next = kth
            prevGr = temp
        return dummy.next

    def getKthNode(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head
        
```

#### 