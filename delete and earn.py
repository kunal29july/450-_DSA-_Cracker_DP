'''
740. Delete and Earn
Medium

3384

223

Add to List

Share
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
'''
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
            This question is similar to https://leetcode.com/problems/house-robber.
            The only difference here is we need to first calculate the money in each house.
            Let us consider, we have houses from 0 to max(nums). Now each time a number occurs in nums, we add that number to its corresponding house.
            At the end we will left with houses and the money they have.
            
        """
        lookup = [0] * (max(nums) + 1)
        for num in nums:
            lookup[num] += 1

        n = len(lookup)
        dp = [0] * n
        dp[0] = lookup[0]
        dp[1] = max(lookup[0], lookup[1])
        for i in range(2, n):
            dp[i] = max(i*lookup[i] + dp[i-2], dp[i-1])
        return dp[-1]
