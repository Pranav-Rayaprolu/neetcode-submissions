class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram is where the frequency of the characters in bogth the strings is equal
        #since this involves frequency we are gonna use hashmap
        if len(s) != len(t):
            return False
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for i in countS:
            #here we are comparing values so we use the following syntax:
            if countS[i] != countT.get(i,0):
                return False
        return True