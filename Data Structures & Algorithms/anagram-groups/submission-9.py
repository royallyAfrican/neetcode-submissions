class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_dict = dict()
        array_list=[]
        idx=0;
        # make string into array_rep
        for word in strs:
            array_rep=[0]*26
            for c in word:
                array_rep[ord(c)-ord('a')]+=1
            if tuple(array_rep) not in group_dict:
                group_dict[tuple(array_rep)]= [strs[idx]]
            else:
                group_dict[tuple(array_rep)].append(strs[idx])
            idx+=1
                
        
        return (list(group_dict.values()))

        
        


        