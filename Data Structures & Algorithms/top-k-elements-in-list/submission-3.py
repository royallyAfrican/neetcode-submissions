class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num_freq=dict()
        output_list=[]
        for num in nums:
            dict_num_freq[num]= dict_num_freq.get(num,0)+1
        tuple_list=(sorted(dict_num_freq.items(),key=lambda x:x[1],reverse=True))
        print(tuple_list)
        for i in range(k):
            x,y=tuple_list[i]
            output_list.append(x)
        return output_list
