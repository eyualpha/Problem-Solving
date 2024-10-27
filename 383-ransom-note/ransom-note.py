class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}
        for i in magazine:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
        for j in ransomNote:
            if j not in store or store[j] == 0:
                return False
            else:
                store[j] -= 1
        return True