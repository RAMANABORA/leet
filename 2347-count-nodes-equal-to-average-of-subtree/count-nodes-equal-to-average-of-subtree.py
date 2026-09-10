# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def trav(node):
            if node is None:
                return (0,0)
            ls ,lc = trav(node.left)
            rs , rc = trav(node.right)
            sts = ls+rs+node.val
            stc = lc+rc+1
            if sts // stc == node.val:
                self.count+=1
            return (sts,stc)
        trav(root)
        return self.count

        
        