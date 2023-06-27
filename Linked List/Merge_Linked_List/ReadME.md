# Merge linked list

### Given the heads of two sorted linked lists, merge them into a single sorted linked list and return the head of the merged list.

```
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ptr = ans = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        while list1:
            ans.next = list1
        while list2:
            ans.next = list2
        return ptr.next
```

#### If the current value of the first list is smaller than the second one, add the node of list one, or vice versa. When we get to the end of one list, add the rest of the other to it. Return the head.