from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        maxAvg = curr_sum / k

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            currAvg = curr_sum / k

            maxAvg = max(maxAvg, currAvg)

        return maxAvg
    

if __name__ == "__main__":
    sol = Solution()
    arr = [1,12,-5,-6,50,3]
    k = 4
    result = sol.findMaxAverage(arr, k)