class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            needed_num= target- nums[i];
            needed_num_index = seen.get(needed_num)
            if(needed_num_index!=None):
                return ([needed_num_index,i]);
            else:
                seen[nums[i]]=i;

        