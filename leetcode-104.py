from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return 1
        result: int = 0
        depth: int = 1
        def dfs(Node: Optional[TreeNode]) -> None:
            nonlocal depth
            nonlocal result
            if not Node.left and not Node.right:
                result = max(depth, result)
                return None
            
            if Node.left:
                depth += 1
                dfs(Node.left)
                depth -= 1

            if Node.right:
                depth += 1
                dfs(Node.right)
                depth -= 1

            return None
        dfs(root)
        return result

'''
同样，要注意nonlocal，即变量的作用范围
'''
            



