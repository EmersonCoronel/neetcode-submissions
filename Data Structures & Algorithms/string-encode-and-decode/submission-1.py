class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        s += "/"
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        current_index = 0
        curr_num = ""
        while current_index < len(s):
            if s[current_index] in "0123456789":
                curr_num += s[current_index]
            elif s[current_index] == "#":
                strs.append(s[current_index + 1 : current_index + 1 + int(curr_num)])
                current_index = current_index + int(curr_num)
                curr_num = ""
            current_index += 1
        return strs
