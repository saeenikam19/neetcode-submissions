class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        for i in range(len(nums)):
            p=1
            for j in range(len(nums)):
                if i!=j:
                    p*=nums[j]
            product.append(p)
        return product