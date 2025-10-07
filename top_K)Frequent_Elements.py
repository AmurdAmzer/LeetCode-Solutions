class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # step 1: create counters
        from collections import Counter
        count = Counter(nums)

        # step 2: create buckets for storing numbers from nums (buckets are just list of arrays [[],[], etc])
        bucket = [[] for i in range(len(nums) + 1)]

        # step 3: store numbers against their frequencies in the buckets
        for number, freq in count.items():
            bucket[freq].append(number)

        # step 4: get results (collect top k from right to left)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for number in bucket[i]:
                res.append(number)
                if len(res) == k:
                    return res