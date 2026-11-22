class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''.join(c for c in s if c in"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        f, l = 0, len(new) - 1
        while (f < l):
            if new[f].lower() != new[l].lower():
                return False
            f += 1
            l -= 1
        return True