# LRU cache

### Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

### Implement the LRUCache class:

### LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
### int get(int key) Return the value of the key if the key exists, otherwise return -1.
### void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
### The functions get and put must each run in O(1) average time complexity.

```
# Time complexity: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

        self.least, self.most = Node(0, 0), Node(0,0)
        self.least.next, self.most.prev = self.most, self.least # Point to each other, if we have one node they will both be attached to it

    def insert(self, node):
        prev, nxt = self.most.prev, self.most 
        prev.next = nxt.prev = node # inserting node in the middle
        node.next, node.prev = nxt, prev # attaching the node to the MRU and previous

    def remove(self, node):
        prev, nxt = node.prev, node.next # get pointers
        prev.next, nxt.prev = nxt, prev # point the pointers to the nodes past the deleted one


    def get(self, key):
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            least = self.least.next
            self.remove(least)
            del self.cache[least.key]
        
```

#### Alright. This problem is more complex but is pretty self explanatory. We need to create a Node class that will be used to keep track of the rank between the most recently used and the least recently used, as well as the value we want to return in case of get. I wrote insert and remove functions as helpers, to improve code readability. The get method will remove and insert again the node in the linked list so that we can refresh its position. We then return its value. The put method checks adds the node to the list. If the list is too long, the LRU node will be removed, and then deleted from the cache.