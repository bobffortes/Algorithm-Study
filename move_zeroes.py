from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        leftmostZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                aux = nums[leftmostZero]
                nums[leftmostZero] = nums[i]
                nums[i] = aux
                leftmostZero += 1

        

if __name__ == "__main__":
    sol = Solution()
    input = [0,1,0,3,12]
    sol.moveZeroes(input)
    print(input)
