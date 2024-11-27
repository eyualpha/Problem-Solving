class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        s,e = 0,0
        max_len = 0
        while e < len(fruits):
            d[fruits[e]] = e
            if len(d) > 2:
                min_val = min(d.values())
                s = min_val + 1
                del d[fruits[min_val]]
            max_len = max(max_len, e - s + 1)
            e += 1
        return max_len
        