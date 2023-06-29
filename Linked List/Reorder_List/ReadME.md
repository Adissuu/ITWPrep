# Reorder List

### Reorder the list to be on the following form:

### L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

```
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def reorderList(self, head):
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head
```
#### This problem actually uses a previous one, the reverse linked list. To solve this one, we implement a tortoise and a hare. When the hare gets to the end of the list, the tortoise is at the middle. We then have to take the second half and reverse it. After that, we simply take one node at a time and remap the linked list. 