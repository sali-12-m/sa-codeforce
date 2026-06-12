class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count=Counter(nums)
        for i,k in count.items():
            if k>len(nums)//2:
                return i
