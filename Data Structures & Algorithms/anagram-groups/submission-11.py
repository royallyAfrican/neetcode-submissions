class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_dict = dict()
        # make string into array_rep
        for word in strs:
            array_rep=[0]*26
            for c in word:
                array_rep[ord(c)-ord('a')]+=1
            if tuple(array_rep) not in group_dict:
                group_dict[tuple(array_rep)]= [word]
            else:
                group_dict[tuple(array_rep)].append(word)
                
        
        return (list(group_dict.values()))

        
        


        