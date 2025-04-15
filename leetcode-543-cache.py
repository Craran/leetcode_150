from typing import Optional
from functools import cache
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        @cache
        def h(node):
            if node == None:
                return -1
            return max(h(node.left), h(node.right)) + 1
        @cache
        def dfs(node):
            if node == None:
                return 0
            return max(h(node.left) + h(node.right) + 2, 
                       dfs(node.left),
                       dfs(node.right))
        
        return dfs(root)
        