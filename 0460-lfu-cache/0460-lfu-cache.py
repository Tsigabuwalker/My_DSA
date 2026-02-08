class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_list = {}

    def _update_freq(self, node):
        freq = node.freq
        self.freq_to_list[freq].remove(node)

        if freq == self.min_freq and self.freq_to_list[freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq_to_list:
            self.freq_to_list[node.freq] = DoublyLinkedList()

        self.freq_to_list[node.freq].add_to_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_freq(node)
            return

        if self.size == self.capacity:
            lfu_list = self.freq_to_list[self.min_freq]
            removed = lfu_list.remove_last()
            del self.key_to_node[removed.key]
            self.size -= 1

        new_node = Node(key, value)
        self.key_to_node[key] = new_node

        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()

        self.freq_to_list[1].add_to_front(new_node)
        self.min_freq = 1
        self.size += 1
