class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        store = {}
        for i in sentence:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        return len(store) == 26