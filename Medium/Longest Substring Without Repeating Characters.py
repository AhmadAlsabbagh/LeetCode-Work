class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        count = 0
        counts = []
        for x in s:
            count += 1
            if x in temp:
                counts.append(len(temp))
                count = 1
                #get rid of the duplicate and everything to the left
                for y in range(len(temp)):
                    if x == temp[y]:
                        temp = temp[y+1:]
                        break
            temp += x
        counts.append(len(temp))
        return max(counts)