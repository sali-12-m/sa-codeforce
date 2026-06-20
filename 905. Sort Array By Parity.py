class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                li.append(nums[i])
        for i in nums:
            if i%2!=0:
                li.append(i)
        return li
