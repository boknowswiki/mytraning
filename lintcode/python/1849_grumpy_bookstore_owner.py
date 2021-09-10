#!/usr/bin/python -t


# two pointers

class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """
    def maxSatisfied(self, customers, grumpy, X):
        # write your code here
        n = len(customers)
        if n == 0:
            return 0

        cur_good_reviews = 0
        for i in range(n):
            if grumpy[i] == 0:
                cur_good_reviews += customers[i]

        max_good_review = 0
        become_good_review = 0
        left = 0

        for right in range(n):
            if grumpy[right] == 1:
                become_good_review += customers[right]

            if right - left +1 > X:
                if grumpy[left] == 1:
                    become_good_review -= customers[left]
                left += 1

            max_good_review = max(max_good_review, become_good_review)

        return  cur_good_reviews+max_good_review
