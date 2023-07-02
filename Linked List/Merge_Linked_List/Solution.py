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
