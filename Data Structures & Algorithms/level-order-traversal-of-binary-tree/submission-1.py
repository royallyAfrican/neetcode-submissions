# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def tr_height(self, tree):
        if tree==None:
            return 0

        
        return 1 + max(self.tr_height(tree.left), self.tr_height(tree.right))

    def tree_traverse(self, curr_level, nested_list, tree):
        if tree==None:
            return;

        nested_list[curr_level].append(tree.val)
        self.tree_traverse( curr_level+1, nested_list, tree.left) 
        self.tree_traverse( curr_level+1, nested_list, tree.right) 
        


        
         
        
          

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # put val at index 0 
        # # populate the list with empty lists
        # # for each subsequent level have a level indicator,(
        # pass level as argument for tree
        # # index into it, and append value to it. 

        nested_list = []
        tree_height= self.tr_height(root)
        for i in range (tree_height):
            nested_list.append([])

        level_indicator = 0
        self.tree_traverse(level_indicator, nested_list, root)
        return nested_list

        