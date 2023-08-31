class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            rev_x = int(str(x)[::-1])
        else:
            rev_x = int(str(x)[::-1][:-1]) * (-1)

        if not (-2 ** 31 <= rev_x < (2 ** 31 - 1)):
            return 0
        else:
            return rev_x