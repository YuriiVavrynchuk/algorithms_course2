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

    def delete(self, data):
        self._root = self._delete(data, self._root)

    def _insert(self, data, root):

        if not root:
            return Node(data)
        elif data < root.data:
            root.left_child = self._insert(data, root.left_child)
        else:
            root.right_child = self._insert(data, root.right_child)

        root.height = 1 + max(self._get_height(root.left_child), self._get_height(root.right_child))

        balance_authenticator = self._get_balance(root)

        if balance_authenticator > 1 and self._get_balance(root.left_child) >= 0:
            return self._right_rotation(root)
        if balance_authenticator < -1 and self._get_balance(root.right_child) <= 0:
            return self._left_rotation(root)
        if balance_authenticator > 1 and self._get_balance(root.left_child) < 0:
            root.left_child = self._left_rotation(root.left_child)
            return self._right_rotation(root)
        if balance_authenticator < -1 and self._get_balance(root.right_child) > 0:
            root.right_child = self._right_rotation(root.right_child)
            return self._left_rotation(root)
        return root

    def _delete(self, data, root):
        if not root:
            return root
        elif data < root.data:
            root.left_child = self._delete(data, root.left_child)
        elif data > root.data:
            root.right_child = self._delete(data, root.right_child)
        else:
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp
            temp = self._get_min_node(root.right_child)
            root.data = temp.data
            root.right_child = self._delete(temp.data, root.right_child)

        if root is None:
            return root

        root.height = 1 + max(self._get_height(root.left_child), self._get_height(root.right_child))
        balance_authenticator = self._get_balance(root)

        if balance_authenticator > 1 and self._get_balance(root.left_child) >= 0:
            return self._right_rotation(root)
        if balance_authenticator < -1 and self._get_balance(root.right_child) <= 0:
            return self._left_rotation(root)
        if balance_authenticator > 1 and self._get_balance(root.left_child) < 0:
            root.left_child = self._left_rotation(root.left_child)
            return self._right_rotation(root)
        if balance_authenticator < -1 and self._get_balance(root.right_child) > 0:
            root.right_child = self._right_rotation(root.right_child)
            return self._left_rotation(root)
        return root

    def _left_rotation(self, z):
        y = z.right_child
        subtree2 = y.left_child

        y.left_child = z
        z.right_child = subtree2

        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))
        return y

    def _right_rotation(self, z):
        y = z.left_child
        subtree3 = y.right_child

        y.right_child = z
        z.left_child = subtree3

        z.height = 1 + max(self._get_height(z.left_child), self._get_height(z.right_child))
        y.height = 1 + max(self._get_height(y.left_child), self._get_height(y.right_child))
        return y

    @staticmethod
    def _get_height(root):
        if not root:
            return 0
        return root.height

    def _get_min_node(self, root):
        if root is None or root.left_child is None:
            return root
        return self._get_min_node(root.left_child)

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left_child) - self._get_height(root.right_child)


if __name__ == '__main__':
    avl_tree = AvlTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)
    avl_tree.delete(30)


