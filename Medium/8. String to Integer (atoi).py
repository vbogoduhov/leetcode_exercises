class Solution:
    def myAtoi(self, s: str) -> int:
        res_str = ''
        flag_digit = False
        for ch in s:
            if not flag_digit:
                if ch == "-":
                    res_str += ch
                elif not ch.isdigit():
                    continue
                else:
                    res_str += ch
                    flag_digit = True
            else:
                if ch.isdigit():
                    res_str += ch
                else:
                    break
        return int(res_str)