# 8. Find Leaves of Binary Tree (https://leetcode.com/problems/find-leaves-of-binary-tree/)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: TreeNode):

        def calHeight(root):
            nonlocal res
            if not root:
                return 0

            height = max(calHeight(root.left), calHeight(root.right)) + 1

            while len(res) < height:
                res.append([])

            res[height-1].append(root.val)

            return height

        res = []
        calHeight(root)
        return res