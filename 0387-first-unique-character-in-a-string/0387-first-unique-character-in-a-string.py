class Solution(object):
    def firstUniqChar(self, s):
        dict={}
        for ch in s:
            dict[ch]=dict.get(ch,0)+1
        for i,ch in enumerate(s):
            if dict[ch]==1:
                return i
        return -1             
        