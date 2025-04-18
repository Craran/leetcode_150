from typing import Optional
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(x, s):
            if x == None:
                return 0
            if s != 0:
                return dfs(x.left, 0) + dfs(x.right, 0) + x.val
            if s == 0:
                return max(dfs(x.left, 0), dfs(x.left, 1)) + max(dfs(x.right, 0), dfs(x.right, 1))
            
        return max(dfs(root, 0), dfs(root, 1))