# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        i = 0
        cur = root
        while cur or stk:
            while cur:
                stk.append(cur)
                cur=cur.left
            cur = stk.pop()
            i += 1
            if i == k:
                return cur.val
            cur = cur.right