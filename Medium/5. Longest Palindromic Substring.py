class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        len_palindrome = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                ss = s[i:j]
                if ss == ss[::-1]:
                    if len(ss) > len_palindrome:
                        palindrome = ss
                        len_palindrome = len(palindrome)

        return palindrome
