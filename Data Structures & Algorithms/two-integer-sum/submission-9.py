class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(0,len(nums)):
            search=target-nums[i]
            if search in hashmap:
                return [hashmap[search],i]
            hashmap[nums[i]]=i      