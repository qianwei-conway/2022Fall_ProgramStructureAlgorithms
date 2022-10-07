# 4. Binary Tree Zigzag Level Order Traversal (https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):

        res = []

        if not root:
            return res

        queue = [root, None]
        sub_res = []
        turn = False

        while queue:

            temp = queue.pop(0)
            if not turn:
                sub_res.append(temp.val)
            else:
                sub_res.insert(0, temp.val)

            if queue[0] == None:
                queue.pop(0)
                res.append(sub_res)
                sub_res = []
                turn = True if turn == False else False
                # turn = !turn

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

            if queue and None not in queue:
                queue.append(None)

        return res









