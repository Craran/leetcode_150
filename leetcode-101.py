from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs_lr(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        if root == None:
            return [None]
        result = []
        stack: List[TreeNode] = [root]
        current = root
        while stack:
            current = stack.pop()
            if current == None:
                result.append(None)
                continue
            result.append(current.val)
            stack.append(current.left)
            stack.append(current.right)
            

        return result
    
    def dfs_rl(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        if root == None:
            return [None]
        result = []
        stack: List[TreeNode] = [root]
        current = root
        while stack:
            current = stack.pop()
            if current == None:
                result.append(None)
                continue
            result.append(current.val)
            stack.append(current.right)
            stack.append(current.left)

        return result


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left = self.dfs_lr(root)
        right = self.dfs_rl(root)
        for i in range(len(left)):
            if left[i] != right[i]:
                return False
            
        return True

