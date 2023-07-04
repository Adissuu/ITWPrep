# Merge K Lists

### You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

### Merge all the linked-lists into one sorted linked-list and return it.


```
class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2): # Merge two lists
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
```

#### We create a new list, (O(n)) and we iterate throught the linked list. If there is a node in List#1, take it in a value, same for List#2. Add them, and if the number is superior than 10, keep a carry that will be added in the next loop. Create a new Node with the value, and update the pointers. Return the head of the new List.