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

        self.least, self.most = Node(0, 0), Node(0, 0)
        # Point to each other, if we have one node they will both be attached to it
        self.least.next, self.most.prev = self.most, self.least

    def insert(self, node):
        prev, nxt = self.most.prev, self.most
        prev.next = nxt.prev = node  # inserting node in the middle
        node.next, node.prev = nxt, prev  # attaching the node to the MRU and previous

    def remove(self, node):
        prev, nxt = node.prev, node.next  # get pointers
        # point the pointers to the nodes past the deleted one
        prev.next, nxt.prev = nxt, prev

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
