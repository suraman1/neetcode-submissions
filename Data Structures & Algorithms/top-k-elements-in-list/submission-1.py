class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        result = []
        bucket = [ []  for _ in range(n + 1)]

        for num, cnt in count.items():
            bucket[cnt].append(num)
        
        m = len(bucket) - 1
        for i in range(m, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result



        