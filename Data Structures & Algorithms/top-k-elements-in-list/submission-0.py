class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            if nums[i] not in check:
                check[nums[i]] = 1
            else:
                check[nums[i]] += 1

        new = sorted(check, key=check.get, reverse=True)
        ret = []
        for i in range(k):
            # return key with highest value from dict, add to list
            ret.append(new[i])

        return ret
             
        