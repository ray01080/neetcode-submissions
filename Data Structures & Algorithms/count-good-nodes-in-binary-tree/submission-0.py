# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        q.append((root, float('-inf')))
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node,maxVal = q.popleft()
                if node:
                    res += 1 if node.val >= maxVal else 0
                    q.append((node.left, max(node.val, maxVal)))
                    q.append((node.right, max(node.val, maxVal)))
        return res