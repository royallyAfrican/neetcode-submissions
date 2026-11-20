class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

    #    sort by x, if tied, place the one with the lower y first
    #    traverse through list of intervals
    #     have list
    #     if x2>=group_x and x2<=group_y group together in list by making max(y2,group_y1) the end
    #     else new list starts with x2.

        intervals= sorted(intervals,key=lambda x: (x[0],x[1])) 
        group_x=intervals[0][0]
        group_y=intervals[0][1]
        res_list=[]
        group_list=[group_x,group_y]
        for i in range(len(intervals)):
            x2 = intervals[i][0]
            y2 = intervals[i][1]
            if x2>=group_x and x2<=group_y:
                group_y= max(group_y,y2)
                group_list=[group_x,group_y]
            else:
                res_list.append(group_list)
                group_x=intervals[i][0]
                group_y=intervals[i][1]
                group_list=[group_x,group_y]
        res_list.append(group_list)
        return res_list

