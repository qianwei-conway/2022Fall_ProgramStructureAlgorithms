# 5. Binary Tree Vertical Order Traversal (https://leetcode.com/problems/binary-tree-vertical-order-traversal/)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return []

        dict = collections.defaultdict(list)
        queue = [[root, 0]]
        min_col = max_col = 0

        while queue:
            node, col = queue.pop(0)

            if node:
                queue.append([node.left, col - 1])
                queue.append([node.right, col + 1])

                dict[col].append(node.val)

                min_col = min(col, min_col)
                max_col = max(col, max_col)

        return [dict[x] for x in range(min_col, max_col + 1)]
