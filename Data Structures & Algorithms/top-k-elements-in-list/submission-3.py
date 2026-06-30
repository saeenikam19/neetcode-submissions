class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        duplicate=[]
        for i in nums:
            if i not in duplicate:
                duplicate.append(i)
        duplicate.sort(key=lambda x: nums.count(x), reverse=True)

        return duplicate[:k]