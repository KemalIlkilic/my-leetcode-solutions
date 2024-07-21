# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans
    def helper(self,root):
        if not root:
            return -1
        left = self.helper(root.left)
        right = self.helper(root.right)
        # check if it is max
        self.ans = max(self.ans,2 + left + right)
        # send to parent node its diameter
        return 1 + max(left, right )