#!/usr/bin/python3 -t

import collections

class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here
        num_list = [n for n in str(num)]
        mono_queue = collections.deque()

        for i, val in enumerate(num_list):
            while mono_queue and num_list[mono_queue[-1]] < val:
                mono_queue.pop()

            mono_queue.append(i)

        for i, val in enumerate(num_list):
            if mono_queue[0] <= i:
                mono_queue.popleft()
                continue

            for j in range(len(num_list)-1, i, -1):
                if num_list[j] == num_list[mono_queue[0]]:
                    num_list[j], num_list[i] = num_list[i], num_list[j]
                    break
            break
        return int("".join(num_list))

if __name__ == '__main__':
    s = Solution()
    a = 2754
    print(s.maximumSwap(a))
    