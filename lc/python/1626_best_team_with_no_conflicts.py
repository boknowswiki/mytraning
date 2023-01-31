
# dp and sort


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ans = 0
        n = len(ages)  # get the number of players
        dp = [0] * n  # initialize dp array to store the maximum total score including the i-th player
        temp = []  # list to store the negated ages and scores of the players
        for i in range(len(scores)):  # loop through all the scores
            temp.append([-ages[i], -scores[i]])  # negating the ages and scores and storing in temp
        temp.sort()  # sort temp based on the first element of each sublist
        for i in range(n):  # loop through all the players
            for j in range(i, -1, -1):  # inner loop to check the maximum total score including j-th player
                if -temp[i][1] <= -temp[j][1]:  # if score of i-th player is less than or equal to j-th player's score
                    dp[i] = max(dp[i], dp[j]-temp[i][1])  # update the maximum total score including i-th player
            ans = max(ans, dp[i])  # update answer with the maximum total score including i-th player
        return ans  # return the final answer
