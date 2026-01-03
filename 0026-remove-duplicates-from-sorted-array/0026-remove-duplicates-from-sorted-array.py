class Solution(object):
    def removeDuplicates(self, nums):
        s=set()
        i=0
        while i in range(len(nums)):
            if  nums[i] in s:
                nums.remove(nums[i])
            else:
                s.add(nums[i])
                i+=1
        return len(nums)        
        