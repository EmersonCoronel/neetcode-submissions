class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for item in strs:
            newitem = ''.join(sorted(item))
            if newitem not in anagrams.keys():
                anagrams[newitem] = [item]
            else:
                anagrams[newitem].append(item)
        return list(anagrams.values())