class Solution:
    def maximum69Number (self, num: int) -> int:
        x = list(map(int, str(num)))
        count = 0
        for i in range(len(x)):
            if x[i] == 9:
                continue
            else:
                x[i] = 9
                break

        y = ''.join(str(x) for x in x)
        return int(y)
        