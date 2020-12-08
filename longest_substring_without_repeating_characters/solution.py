def lengthOfLongestSubstring(self, s: str) -> int:
    substring = []
    res = 0
    
    for i in s:
        if i in substring:
            index = substring.index(i)
            substring = substring[index+1:]
        substring.append(i)
        res = max(len(substring), res)
        
    return res