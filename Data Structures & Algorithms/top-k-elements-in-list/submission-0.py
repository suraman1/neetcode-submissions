class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count.items(), key=lambda a: a[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_count[i][0])
        return result

        