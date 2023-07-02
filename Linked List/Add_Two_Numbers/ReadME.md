# Add two number

### You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


```
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```

#### We create a new list, (O(n)) and we iterate throught the linked list. If there is a node in List#1, take it in a value, same for List#2. Add them, and if the number is superior than 10, keep a carry that will be added in the next loop. Create a new Node with the value, and update the pointers. Return the head of the new List.