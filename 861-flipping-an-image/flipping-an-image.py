class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for i in image:
            j = i.reverse()
            c = []
            for j in range(len(i)):
                if i[j] == 1:
                    c.append(0)
                else:
                    c.append(1)
            result.append(c)
        return result

        