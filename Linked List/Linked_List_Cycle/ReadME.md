# Linked List Cycle

### Given head, the head of a linked list, determine if the linked list has a cycle in it.

### There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

### Return true if there is a cycle in the linked list. Otherwise, return false.

### Solution 1
```
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def hasCycle(self, head):
        tracker = set()

        current = head
        while current:
            if current in tracker: return True
            tracker.add(current)
            current = current.next
        
        return False
```
### Solution 2
```
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

#### In the first solution, we create a set, and add the current node we're on in the set. We then check if it the next node is already in the set. If it is return True, else continue. This can be further optimized by removing the necessity of a set, and introducing two pointers, like in the second solution. In this one, we need n-1 iterations to know if the linked list contains a loop, since the two pointers would meet again. (n = 25, 25 + 1 - 2, etc.) 