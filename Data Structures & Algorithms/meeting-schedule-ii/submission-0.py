"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        days = [[] for i in range(len(intervals))]

        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            start = interval.start
            end = interval.end

            for day in days:
                if len(day) == 0:
                    day.append(interval)
                    break
                else:
                    # check if interval can fit in this day
                    prev_start = day[-1].start
                    prev_end = day[-1].end

                    if prev_start <= prev_end <= start <= end:
                        # valid interval for this day
                        day.append(interval)
                        break
        
        # get the num of days we used
        output = 0
        for day in days:
            if len(day) != 0:
                output += 1
        print(days)
        return output
        
            

        