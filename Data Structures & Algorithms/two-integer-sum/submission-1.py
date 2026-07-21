class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                if prevMap[diff]<i:
                    return [prevMap[diff],i]
                else:
                    return [i,prevMap[diff]]

            prevMap[n] = i

        return []