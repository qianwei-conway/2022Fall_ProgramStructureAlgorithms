# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        def _postorder(root):
            return _postorder(root.left) + _postorder(root.right) + [str(root.val)] if root else []

        return ','.join(_postorder(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        def _build_BST(low=-math.inf, up=math.inf):
            if not arr or arr[-1] < low or arr[-1] > up:
                return None

            num = arr.pop()
            root = TreeNode(num)
            root.right = _build_BST(num, up)
            root.left = _build_BST(low, num)

            return root

        arr = [int(x) for x in data.split(',') if x]
        return _build_BST()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans