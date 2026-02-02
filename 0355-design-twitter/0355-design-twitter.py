import heapq

class Twitter:
    def __init__(self):
        # Store tweets: userId -> list of (timestamp, tweetId)
        self.tweets = {}
        
        # Store followers: userId -> set of followeeIds
        self.followees = {}
        
        # Global timestamp to maintain tweet order
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        # Store with decreasing timestamp for max-heap
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # Users to consider: self + followees
        users = self.followees.get(userId, set()).copy()
        users.add(userId)
        
        heap = []
        # Add the most recent tweet of each user to heap
        for u in users:
            if u in self.tweets:
                for t, tweetId in self.tweets[u]:
                    heapq.heappush(heap, (-t, tweetId))  # max-heap using negative timestamp
        
        # Extract 10 most recent tweets
        res = []
        for _ in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return  # Cannot follow self
        if followerId not in self.followees:
            self.followees[followerId] = set()
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees:
            self.followees[followerId].discard(followeeId)
