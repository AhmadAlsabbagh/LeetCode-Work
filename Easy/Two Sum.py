class Solution:
    def twoSum(self, nums, target):
        if len(nums) < 2:
            pass
        tempDict = {}
        for i in range(len(nums)):
            checkNum = target-nums[i]
            if(checkNum in tempDict.keys()):
                if i < tempDict[checkNum]:
                    return [i, tempDict[checkNum]]
                else:
                    return [tempDict[checkNum], i]
            else:
                tempDict[nums[i]] = i