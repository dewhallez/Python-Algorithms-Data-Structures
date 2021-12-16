# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        return self.Helper(root.left, root.right)
    
    def Helper(self, left, right):
        if left == None or right == None:
            return left == right
        if left.val != right.val:
            return False
        
        return self.Helper(left.left,right.right) and self.Helper(left.right, right.left)