# 3. Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):

        res = []
        if not root:
            return res

        queue = [root, None]

        while queue:
            temp = queue.pop(0)
            if queue[0] == None:
                queue.pop(0)
                res.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            if queue and None not in queue:
                queue.append(None)

        return res