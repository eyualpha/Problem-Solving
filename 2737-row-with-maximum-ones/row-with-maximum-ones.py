class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        s = [0]*2
        count = 0
        for i in range(len(mat)):       
            if mat[i].count(1) > count:
                count = mat[i].count(1)
                s[0] = i
                s[1] = count
        return s
            
            
        