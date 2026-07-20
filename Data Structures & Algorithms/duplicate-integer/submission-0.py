class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap={} #index : val

        for n in nums: 
            if n in hashMap:
                return True
            hashMap[n]=True
        return False
        