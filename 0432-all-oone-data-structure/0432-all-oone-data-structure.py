class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Node(0)  # Sentinel head
        self.tail = Node(0)  # Sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapping = {}  # key -> Node

    def _add_node_after(self, new_node, prev_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.mapping:
            # Insert after head if count 1 node doesn't exist
            if self.head.next.count != 1:
                self._add_node_after(Node(1), self.head)
            self.head.next.keys.add(key)
            self.mapping[key] = self.head.next
        else:
            curr_node = self.mapping[key]
            next_count = curr_node.count + 1
            if curr_node.next.count != next_count:
                self._add_node_after(Node(next_count), curr_node)
            curr_node.next.keys.add(key)
            self.mapping[key] = curr_node.next
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove_node(curr_node)

    def dec(self, key: str) -> None:
        curr_node = self.mapping[key]
        if curr_node.count == 1:
            del self.mapping[key]
        else:
            prev_count = curr_node.count - 1
            if curr_node.prev.count != prev_count:
                self._add_node_after(Node(prev_count), curr_node.prev)
            curr_node.prev.keys.add(key)
            self.mapping[key] = curr_node.prev
        
        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        # Return any key from the set
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))