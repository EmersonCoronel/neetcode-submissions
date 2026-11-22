class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        i, j, longest, curr = 0, 1, 1, 1
        while j < len(s):
            # print(i, j, curr, s[i], s[j])
            if s[j] not in s[i : j]:
                curr += 1
                if curr > longest:
                    longest = curr
                j += 1
            else:
                if curr != 1:
                    curr -= 1
                i += 1
                if i == j:
                    j = i + 1
        return longest