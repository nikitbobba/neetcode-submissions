class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minCount = 0
        l = 0
        for i in range(1, len(intervals)):
            # if the current interval is non overallpoing with previous
            # increment count
            currStart, currEnd = intervals[i]
            prevStart, prevEnd = intervals[l]

            if currStart < prevEnd:
                minCount += 1

                # which do i remove?
                # the one that starts later
                if prevEnd > currEnd:
                    # got to curr end
                    l = i
                else:
                    # do nothing
                    continue
            else:
                l=i

            # otherwise move on
        return minCount


        