# Copy list with random pointer

### Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.


```
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def copyRandomList(self, head):
        oldToCopy = {None : None}
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
```

#### We need two passes in the array. First of all, we create a copy node with the value of the current node in a hashmap. We then pass again and making the connections. We then return the head of the new List.