"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prev_start, prev_end = None, None
        for interval in intervals:
            start = interval.start
            end = interval.end
            if (prev_start is None or prev_end is None) or (prev_start <= prev_end <= start <= end):
                prev_start = start
                prev_end = end
                continue
            else:
                return False
        
        return True

