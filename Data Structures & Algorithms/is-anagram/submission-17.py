#probalbly something where we create a dictionary maybe 2.  
# on dic per word. letter is the key and the other number is the count
# if i in word is in dic, add 1 to the count else add letter to dic
# and set count to 1. then once both words are iterated through,
# see equality between dictionaries. 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        tdic = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in sdic:
                sdic[i] += 1
            else:
                sdic[i] = 1
        for x in t:
            if x in tdic:
                tdic[x] += 1
            else:
                tdic[x] = 1
        if sdic == tdic:
            return True
        else:
            return False
        
            