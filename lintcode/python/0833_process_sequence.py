#!/usr/bin/python -t

# sweep line scan and hash map solution


class Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    def numberOfProcesses(self, logs, queries):
        # Write your code here
        time = []

        # 0: end, 1: start, 2: in progress
        for log in logs:
            time.append((log[0], 1))
            time.append((log[1] + 1, 0))
            
        #print time

        for t in queries:
            time.append((t, 2))
        #print time
        time.sort()
        #print time
        cnt = 0
        time2cnt = {}

        for t, status in time:
            if status == 0:
                cnt -= 1
            elif status == 1:
                cnt += 1

            time2cnt[t] = cnt
        #print time2cnt
        return [time2cnt[t] for t in queries]

if __name__ == '__main__':
    s = [(323590401,608580695),(680417571,740927995),(8000719,95236027),(364293775,1052503147),(25960936,731655112),(75634358,115570826),(27303361,716044243),(266725056,567494217),(2255907,44836419),(90803241,265311561)]
    t = [138303481,305539591,138113185,102644275,653265601,241720193,188734546,123232425,322162573,528753202,436683931,153333603,686299562]
    ss = Solution()
    print "answer is\n"
    print ss.numberOfProcesses(s, t)
