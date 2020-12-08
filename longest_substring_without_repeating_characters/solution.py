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

# Solution 2, optimized
def lengthOfLongestSubstring2(self, s: str) -> int:
    dic, res, start = {}, 0, 0
    
    for i, ch in enumerate(s):
        if ch in dic:
            res = max(res, i-start)         # res can be calculated after each iteration
            start = max(start, dic[ch] + 1) # abba
        dic[ch] = i
        
    return max(res, len(s)-start)