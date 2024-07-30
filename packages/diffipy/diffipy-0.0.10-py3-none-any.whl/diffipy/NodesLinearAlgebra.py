from .Node import *


class DotProductNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__()
        self.left = self.ensure_node(left)
        self.right = self.ensure_node(right)
        self.parents = [self.left, self.right]


    def __str__(self):
        return f"dotProduct({str(self.left)},{str(self.right)})"
