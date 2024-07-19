from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive
        '''
        if not root:
            return
        elif not root.left and not root.right:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        '''
        #dfs
        '''
        stack = deque([root])
        while stack:
            curr = stack.pop()
            if curr:
                stack.append(curr.right)
                stack.append(curr.left)
                curr.left, curr.right = curr.right, curr.left
        return root
        '''
        #bfs

        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
                curr.left, curr.right = curr.right, curr.left
        return root
