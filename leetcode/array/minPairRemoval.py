from typing import List

class Solution:
    def checkSorted(self, nums):
        for i in range (0, len(nums) - 1, 1):
            if (nums[i] > nums[i + 1]):
                return False
        return True
    
    def replaceInArray(self, nums, index, sum):
        print (f"Replacing INDEX: {index}")
        nums[index] = sum
        del nums[index + 1]


    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        countOp = 0

        while not self.checkSorted(nums):
            print("----- NOT SORTED YET -----")
            print(nums)
            minSum = float("inf")
            i = 0
            index = 0
            while i < len(nums) - 1 :
                currSum = nums[i] + nums[i+1]
                if (minSum > currSum):
                    print(f"Sum between {nums[i]} + {nums[i+1]} at indexes {i} and {i + 1}")
                    print(f"Replace MinSum: {minSum} with CurrSum {currSum}")
                    minSum = currSum
                    index = i
                i += 1
            
            self.replaceInArray(nums, index, minSum)

            print("\n ----- END OF OPERATION -----")
            countOp += 1

        return countOp
    

if __name__ == "__main__":
   
    arr = [-2,1,2,-1,-1,-2,-2,-1,-1,1,1]
    sol = Solution()

    result = sol.minimumPairRemoval(arr)
    print(result)
