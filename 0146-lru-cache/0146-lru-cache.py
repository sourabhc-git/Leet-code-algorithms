class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache with a fixed capacity.
        """
        self.capacity = capacity
        self.cache = {}  # Hash map to store key -> Node
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node: Node):
        """Add a node to the end of the doubly linked list."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        """
        Retrieve the value associated with the key if it exists in the cache.
        If the key does not exist, return -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Remove it from its current position
            self._add(node)    # Move it to the end (most recently used)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value associated with the key.
        If the cache exceeds the capacity, evict the least recently used item.
        """
        if key in self.cache:
            self._remove(self.cache[key])  # Remove the existing node
        node = Node(key, value)
        self._add(node)  # Add the new node
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Evict the least recently used item (head's next node)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


