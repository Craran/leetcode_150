from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        sum = root.val
        flag = False
        
        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal sum
            nonlocal targetSum
            nonlocal flag
            if root.left == None and root.right == None:
                
                if sum == targetSum:
                    flag = True
                return None
            if root.left != None:
                sum += root.left.val
                dfs(root.left)
                sum -= root.left.val
            if root.right != None:
                sum += root.right.val
                dfs(root.right)
                sum -= root.right.val

        dfs(root)
        return flag
            
            
            


            
