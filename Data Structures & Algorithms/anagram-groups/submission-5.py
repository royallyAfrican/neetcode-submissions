class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list=defaultdict(list)
        for word in strs:
            dict_key= "".join(sorted(word))
            dict_list[dict_key].append(word)
        big_list=[]
        for key in dict_list:
            big_list.append(dict_list.get(key))
        return big_list