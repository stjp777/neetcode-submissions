from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for num in nums:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1
        
        result = []
        f = sorted(f, key=lambda x: f[x], reverse=True)
        return f[:k]