class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}
        note = {}
        for i in magazine:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
        # for j in ransomNote:
        #     if j not in note:
        #         note[j] = 1
        #     else:
        #         note[j] += 1
        # for k in ransomNote:
        #     if k not in store or note[k] > store[k]:
        #         return False
        # return True
        for j in ransomNote:
            if j not in store or store[j] == 0:
                return False
            else:
                store[j] -= 1
        return True

