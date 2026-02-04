class TopVotedCandidate:

    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        count = {}  # candidate -> votes
        leader = None
        max_votes = 0

        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= max_votes:
                # If tie, most recent vote wins
                leader = p
                max_votes = count[p]
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        # Binary search for the largest index i where times[i] <= t
        left, right = 0, len(self.times) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] <= t:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.leaders[ans]
