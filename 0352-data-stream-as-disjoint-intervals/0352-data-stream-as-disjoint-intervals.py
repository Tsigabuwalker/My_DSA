class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        n = len(intervals)

        i = 0
        while i < n:
            start, end = intervals[i]

            if start <= value <= end:
                return

            if value == end + 1:
                intervals[i][1] = value
                if i + 1 < n and intervals[i + 1][0] == value + 1:
                    intervals[i][1] = intervals[i + 1][1]
                    intervals.pop(i + 1)
                return

            if value + 1 == start:
                intervals[i][0] = value
                return

            if value < start:
                intervals.insert(i, [value, value])
                return

            i += 1

        intervals.append([value, value])

    def getIntervals(self):
        return self.intervals
