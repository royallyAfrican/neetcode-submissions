class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        # iterate store each char in a set to check if seen
        # if seen,(compute current max)
        # move l pointer, 
        # move r pointer
        # return max when l>r

        l = 0
        r = 0
        seen= set()
        maximum=0
        
        while(r<len(s)):
            sub = s[l:r] 
            while(s[r] in seen):
                seen.remove(s[l])
                l+=1
                
            maximum=max(r+1-l, maximum)
            seen.add(s[r])
            r+=1
        return maximum




        