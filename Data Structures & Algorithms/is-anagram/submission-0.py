class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters={}

       #Edge case
        if len(s)!=len(t):
            return False
        
        for i in s:
            if i  not in letters:
                letters[i]=1
            else:
                letters[i]+=1

        for i in t:
            if i not in letters:
                return False
            else:
                letters[i]-=1
            if letters[i]<0:
                return False
        return True

