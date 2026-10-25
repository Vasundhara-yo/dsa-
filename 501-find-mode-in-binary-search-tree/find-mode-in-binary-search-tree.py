# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:

        freq = {}
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            freq[node.val] = freq.get(node.val, 0) + 1
            inorder(node.right)
        
        inorder(root)
        
        max_freq = max(freq.values())
        
        ans = []
        for key in freq:
            if freq[key] == max_freq:
                ans.append(key)
        
        return ans

        