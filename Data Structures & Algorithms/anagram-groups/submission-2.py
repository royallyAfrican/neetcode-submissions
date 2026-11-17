class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_list=[]
        d={}
        for word in strs:
            d[word]=d.get(word,0)+1

        for i in range(len(strs)):
            sublist=[strs[i]]
            for j in range(i+1,len(strs),1):
                if( (d.get(strs[j])>0) and 
                    sorted(strs[i])==sorted(strs[j])):
                    sublist.append(strs[j])
                    d[strs[j]]= d.get(strs[j])-1
            if(d.get(strs[i])>0):
                big_list.append(sublist)
                d[strs[i]]= d.get(strs[i])-1
            

        return big_list