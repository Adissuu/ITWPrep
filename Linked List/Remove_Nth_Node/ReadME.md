# Remove nth Node

### Given the head of a linked list, remove the nth node from the end of the list and return its head.

```
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        hat = ListNode(42, head)
        left = hat
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return hat.next
```

#### Create a dummy head that will force the left pointer to be before the node we want to remove. We then create the offset based on n, and we proceed to the execution. At the end, we skip the node we want to remove.