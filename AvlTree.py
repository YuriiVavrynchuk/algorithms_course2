class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


class AvlTree:
    def __init__(self):
        self._root = None

    def insert(self, data):
        self._root = self._insert(data, self._root)

    def _insert(self, data, root):

        if not root:
            return Node(data)
        elif data < root.data:
            root.left_child = self._insert(data, root.left_child)
        else:
            root.right_child = self._insert(data, root.right_child)

        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))

        balance_authenticator = self.get_balance(root)

        if balance_authenticator > 1 and data < root.left_child.data:
            return self.right_rotation(root)

        if balance_authenticator < -1 and data > root.right_child.data:
            return self.left_rotation(root)

        if balance_authenticator > 1 and data > root.left_child.data:
            root.left_child = self.left_rotation(root.left_child)
            return self.right_rotation(root)

        if balance_authenticator < -1 and data < root.right_child.data:
            root.right_child = self.right_rotation(root.right_child)
            return self.left_rotation(root)

        return root

    def left_rotation(self, z):
        y = z.right_child
        subtree2 = y.left_child

        y.left_child = z
        z.right_child = subtree2

        z.height = 1 + max(self.get_height(z.left_child),
                           self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child),
                           self.get_height(y.right_child))
        return y

    def right_rotation(self, z):
        y = z.left_child
        subtree3 = y.right_child

        y.right_child = z
        z.left_child = subtree3

        z.height = 1 + max(self.get_height(z.left_child),
                           self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child),
                           self.get_height(y.right_child))
        return y

    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left_child) - self.get_height(root.right_child)


if __name__ == '__main__':
    avl_tree = AvlTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

