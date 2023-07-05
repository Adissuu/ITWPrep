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
