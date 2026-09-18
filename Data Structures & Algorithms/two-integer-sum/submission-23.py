class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            n = nums[i]
            need = target - n

            if need in seen: # search dict value
                return [seen[need], i]
            
            seen[n] = i
