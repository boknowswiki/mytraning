# sort
# time O(nlogn)
# space O(1)

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n < 2:
            return True

        intervals.sort()

        for i in range(1, n):
            if intervals[i-1][1] > intervals[i][0]:
                return False

        return True
      
# time O(n)
# space O(n)
      
public bool CanAttendMeetings(int[][] intervals) {
        var arr = new int[1000001];
        for(int i = 0; i < intervals.Length; i++)
        {
            arr[intervals[i][0]]++;
            arr[intervals[i][1]]--;
        }
        
        for(int i = 1; i < arr.Length; i++)
        {
            arr[i] += arr[i-1];
            if(arr[i] > 1) return false;
        }
        
        return true;
    }
	
