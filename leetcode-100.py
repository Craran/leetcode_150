from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], arr: List[Optional[int]]) -> None:
        if root == None:
            arr.append(None)
            return None
        arr.append(root.val)
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)




    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr_p = []
        arr_q = []
        self.dfs(p, arr_p)
        self.dfs(q, arr_q)
        if len(arr_p) != len(arr_q):
            return False
        for i in range(len(arr_p)):
            if arr_p[i] != arr_q[i]:
                return False

        return True
