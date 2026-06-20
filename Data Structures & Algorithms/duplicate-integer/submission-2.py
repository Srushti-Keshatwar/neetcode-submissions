class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left=0
        right=len(nums)-1
        count=1
        set_d=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
        if count>1 :
            return True
        else:
            return False
        