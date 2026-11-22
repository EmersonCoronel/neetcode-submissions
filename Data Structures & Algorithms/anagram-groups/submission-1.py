class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        if len(strs) == 0:
            return []
        for item in strs:
            flag = False
            for index in range(len(anagrams)):
                if len(item) == len(anagrams[index][0]):
                    if sorted(item) == sorted(anagrams[index][0]):
                        anagrams[index].append(item)
                        flag = True
                        continue
            if flag == False:
                anagrams.append([item])
        return anagrams


    def checkAnagram(self, strs: List[str]) -> bool:
        return sorted(strs[0]) == sorted(strs[1])