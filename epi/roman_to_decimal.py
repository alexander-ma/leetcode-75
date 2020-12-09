# See Leetcode No. 13
def romanToInt(self, s: str) -> int:
    # 'I', 'V', 'X', 'L', 'C', 'D', 'M'
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    if len(s) == 1:
        return d[s]
    
    res = 0
    
    prev = 1001
    curr = 0
    for ch in s:
        curr = d[ch]
        if prev >= curr:
            res += curr
        else:
            res = (res - prev) + (curr - prev)
        prev = curr
            
    return res