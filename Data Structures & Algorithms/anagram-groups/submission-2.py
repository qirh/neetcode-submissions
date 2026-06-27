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

        for word in strs:
            found_anagram = False
            for l in res:
                if len(l) > 0:
                    if self.isAnagram(l[0], word):
                        l.append(word)
                        found_anagram = True
                        break
            
            if not found_anagram:
                res.append([word])

        return res
        