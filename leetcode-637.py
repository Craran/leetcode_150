from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        result: List[float] = []
        q = deque()

        q.appendleft((root, 0))
        cal: List[int, int, int] = [-1, 0, 1] # [layer, value, cnt]

        while q:
            now, layer = q[-1][0], q[-1][1]
            q.pop()
            if layer != cal[0]:
                result.append(float(cal[1]) / cal[2])
                cal[0], cal[1], cal[2] = layer, now.val, 1
            else:
                cal[1], cal[2] = cal[1] + now.val, cal[2] + 1
            
            if now.left != None:
                q.appendleft((now.left, layer + 1))
            
            if now.right != None:
                q.appendleft((now.right, layer + 1))
            
            if not q:
                result.append(float(cal[1]) / cal[2])
        
        return result[1: ]
                

            



        ...
