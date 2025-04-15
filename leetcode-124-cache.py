from typing import Optional
from functools import cache
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        @cache
        def h(node):
            if node == None:
                return 0
            return max(max(h(node.left), h(node.right)) + node.val, 0)
        
        @cache
        def dfs(node):
            if node == None:
                return -inf
            res = h(node.left) + h(node.right) + node.val

            if node.left != None:
                res = max(res, dfs(node.left))

            if node.right != None:
                res = max(res, dfs(node.right))
            return res
        
        return dfs(root)
    

