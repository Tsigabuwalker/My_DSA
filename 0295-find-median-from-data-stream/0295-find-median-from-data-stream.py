class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def _push(self, heap, val, is_max_heap):
        heap.append(val)
        curr = len(heap) - 1
        while curr > 0:
            parent = (curr - 1) // 2
            if (is_max_heap and heap[curr] > heap[parent]) or \
               (not is_max_heap and heap[curr] < heap[parent]):
                heap[curr], heap[parent] = heap[parent], heap[curr]
                curr = parent
            else:
                break

    def _pop(self, heap, is_max_heap):
        if not heap: return None
        if len(heap) == 1: return heap.pop()
        res = heap[0]
        heap[0] = heap.pop()
        self._sift_down(heap, 0, is_max_heap)
        return res

    def _sift_down(self, heap, curr, is_max_heap):
        while True:
            left, right = 2 * curr + 1, 2 * curr + 2
            target = curr
            if left < len(heap):
                if (is_max_heap and heap[left] > heap[target]) or \
                   (not is_max_heap and heap[left] < heap[target]):
                    target = left
            if right < len(heap):
                if (is_max_heap and heap[right] > heap[target]) or \
                   (not is_max_heap and heap[right] < heap[target]):
                    target = right
            if target != curr:
                heap[curr], heap[target] = heap[target], heap[curr]
                curr = target
            else:
                break

    def addNum(self, num: int) -> None:
        self._push(self.small, num, True)
        self._push(self.large, self._pop(self.small, True), False)

        if len(self.large) > len(self.small):
            self._push(self.small, self._pop(self.large, False), True)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(self.small[0])
        return (self.small[0] + self.large[0]) / 2.0