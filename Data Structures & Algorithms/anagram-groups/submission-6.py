class Solution:

    def isAnagram(self, str1: str, str2: str) -> bool:

        if len(str1) != len(str2):
            return False
        if str1 == str2:
            return True
        
        d1 = dict()
        d2 = dict()

        for i in range(len(str1)):
            c1 = str1[i]
            c2 = str2[i]
            d1[c1] = d1.get(c1, 0) + 1
            d2[c2] = d2.get(c2, 0) + 1
        return d1 == d2


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in d:
                i = d[sorted_word]
                res[i].append(word)
            else:
                d[sorted_word] = len(res)
                res.append([word])
        return res
        