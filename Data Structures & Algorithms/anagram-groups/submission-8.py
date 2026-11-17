class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_dict = dict()
        array_list=[]
        # make string into array_rep
        for word in strs:
            array_rep=[0]*26
            for c in word:
                array_rep[ord(c)-ord('a')]+=1
            array_list.append(array_rep)
        
        for i in range (len(array_list)):
            if tuple(array_list[i]) not in group_dict:
                group_dict[tuple(array_list[i])]= [strs[i]]
            else:
                group_dict[tuple(array_list[i])].append(strs[i])
        
        return (list(group_dict.values()))

        
        


        