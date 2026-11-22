class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += word
            s += "/space/"
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        start_index = 0
        current_index = 0
        while current_index < len(s) - 6:
            if s[current_index] == '/' and s[current_index + 6] == '/':
                strs.append(s[start_index:current_index])
                current_index = current_index + 7
                start_index = current_index
            else:
                current_index += 1
        return strs
