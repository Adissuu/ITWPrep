# Reverse linked list

### Given the head of a singly linked list, reverse the list, and return the reversed list.

```
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
```

#### While there current is a node, we save the next node -> the next node is the previous (breaking the old link and adding it to the previous) -> the previous node is now the current one -> the current is now the next in the list -> repeat till the end