class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1. Create a hashmap and a helper array
        hmp = {}

        # 2. Count the numbers in the hashmap
        for num in nums:
            hmp[num] = hmp.get(num, 0) + 1

        # 3. Create a list of tuples from the dictionary and sort them in descending order AND by the second value of the tuple 
        # (KEY, VALUE) --> lambda t:t[1] gets the second val
        ans = list(hmp.items())
        ans.sort(key=lambda t:t[1], reverse=True)

        # 4. Return the keys of the first K elem
        return [key[0] for key in ans[:k]]