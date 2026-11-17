class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_list = []
        dict_groups=dict()

        for word in strs:
            word_26=[]
            for i in range(26):
                word_26.append(0)
            for c in word:
                word_26[ord(c)-ord('a')]+=1
            word_list.append(word_26)

        for i in range(len(word_list)):
            if(dict_groups.get(tuple(word_list[i]))==None):
                dict_groups[tuple(word_list[i])]=[strs[i]]
            else:
                dict_groups[tuple(word_list[i])].append(strs[i])

        return list(dict_groups.values())

        
