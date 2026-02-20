class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def add(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for num in bucket:
            if num == key:
                return
        bucket.append(key)

    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                return

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for num in bucket:
            if num == key:
                return True
        return False