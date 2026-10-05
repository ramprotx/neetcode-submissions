class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        'count or defaultdict'
        hashmap={}
        hashmap=Counter(nums)
        return [item[0] for item in hashmap.most_common(k)]