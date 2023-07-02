# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def copyRandomList(self, head):
        oldToCopy = {None: None}
        ptr = head
        while ptr:
            copy = Node(ptr.val)
            oldToCopy[ptr] = copy
            ptr = ptr.next
        ptr = head
        while ptr:
            copy = oldToCopy[ptr]
            copy.next = oldToCopy[ptr.next]
            copy.random = oldToCopy[ptr.random]
            ptr = ptr.next
        return oldToCopy[head]
