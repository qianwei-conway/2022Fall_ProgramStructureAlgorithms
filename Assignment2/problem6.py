# 6. Maximum Width of Binary Tree (https://leetcode.com/problems/maximum-width-of-binary-tree/)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode):

        res = 1
        queue = [[root, 0]]

        while queue:
            level_length = len(queue)
            _, index_of_left = queue[0]

            for _ in range(level_length):
                node, index = queue.pop(0)

                if node.left:
                    queue.append([node.left, 2*index])
                if node.right:
                    queue.append([node.right, 2*index+1])

            res = max(res, index - index_of_left + 1)

        return res