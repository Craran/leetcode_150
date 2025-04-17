from typing import List
from functools import cache
from math import inf


class Solution:
    # @staticmethod
    def longestPath(self, parent: List[int], s: str) -> int:
        n, ns = len(parent), len(s)
        tree = {}
        for i, x in enumerate(parent):
            if x not in tree:
                tree[x] = [i]
            else:
                tree[x].append(i)

        
        @cache
        def h(node):
            if node not in tree:
                return 1
            res = 0
            for sub_node in tree[node]:
                if s[node] != s[sub_node]:
                    res = max(res, h(sub_node) + 1)
            return res if res != 0 else 1
        
        @cache
        def dfs(node):
            res = 0
            if node not in tree:
                
                return 1
            
            chain = [0, 0]
            res = 0
            for sub_node in tree[node]:
                if s[node] != s[sub_node]:
                    if h(sub_node) >= chain[1]:
                        chain[0], chain[1] = chain[1], chain[0]
                        chain[1] = h(sub_node)
                    elif h(sub_node) > chain[0]:
                        chain[0] = h(sub_node)
                    
            
            res = max(res, chain[0] + chain[1] + 1)

            for sub_node in tree[node]:
                res = max(res, dfs(sub_node))
            
            return res
        return dfs(0)

            
# # Solution.longestPath(None, [-1,0,0,0], "aabc")


from typing import List
from functools import cache

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        tree = {}
        for i, x in enumerate(parent):
            if x not in tree:
                tree[x] = []
            tree[x].append(i)
        
        @cache
        def h(node):
            if node not in tree:
                return 1
            max_length = 0
            for sub_node in tree[node]:
                if s[node] != s[sub_node]:
                    max_length = max(max_length, h(sub_node) + 1)
            return max_length if max_length != 0 else 1  # 至少包含当前节点
        
        @cache
        def dfs(node):
            max1 = 0
            max2 = 0
            if node in tree:
                for sub_node in tree[node]:
                    if s[node] != s[sub_node]:
                        current_h = h(sub_node)
                        if current_h > max1:
                            max2 = max1
                            max1 = current_h
                        elif current_h > max2:
                            max2 = current_h
            res = max1 + max2 + 1  # 穿过当前节点的路径长度
            if node in tree:
                for sub_node in tree[node]:
                    res = max(res, dfs(sub_node))
            return res
        
        return dfs(0)


from typing import List
from functools import cache
from math import inf

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = {}

        for i, x in enumerate(parent):
            if x not in tree:
                tree[x] = [i]
            else:
                tree[x].append(i)

        ans = 0
        @cache
        def dfs(node):
            nonlocal ans
            if node not in tree:
                return 0
            link = 0
            for sub_node in tree[node]:
                if s[node] != s[sub_node]:
                    sub_link = dfs(sub_node) + 1
                    
                    ans = max(ans, link + sub_link)
                    link = max(link, sub_link)

            return link
        dfs(0)
        return ans + 1

                    

