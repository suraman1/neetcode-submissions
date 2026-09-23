class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, value in enumerate(nums):
            
            if target - value in indexes:
                return [indexes[target - value], i]
            
            indexes[value] = i

        
        