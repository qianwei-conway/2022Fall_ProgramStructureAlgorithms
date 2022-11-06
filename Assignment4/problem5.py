# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.store = []
        self.index = -1

        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.store.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.store[self.index]

    def hasNext(self) -> bool:
        return len(self.store) - 1 > self.index

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()