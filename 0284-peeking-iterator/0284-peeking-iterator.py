class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        self._next = iterator.next() if iterator.hasNext() else None  # cache the next element

    def peek(self) -> int:
        """
        Returns the next element without advancing the iterator.
        """
        return self._next

    def next(self) -> int:
        """
        Returns the next element and advances the iterator.
        """
        current = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self) -> bool:
        """
        Returns True if there are more elements.
        """
        return self._next is not None
