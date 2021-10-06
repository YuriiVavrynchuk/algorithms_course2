class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self, root_element: Node):
        self.root = root_element

    def inorder(self, node: Node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node

    def delete_node(self, node: Node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self.delete_node(node.left, data)
            return node

        elif data > node.data:
            node.right = self.delete_node(node.right, data)
            return node

        if node.left is None and node.right is None:
            return None

        if node.left is None:
            temp = node.right
            node = None
            return temp

        elif node.right is None:
            temp = node.left
            node = None
            return temp

        succ_parent = node

        succ = node.right

        while succ.left is not None:
            succ_parent = succ
            succ = succ.left

        if succ_parent != node:
            succ_parent.left = succ.right
        else:
            succ_parent.right = succ.right

        node.key = succ.data

        return node


if __name__ == '__main__':
    fruits = BinarySearchTree(Node(23))
    fruits.insert(fruits.root, 5)
    fruits.insert(fruits.root, 12)
    fruits.insert(fruits.root, 100)
    fruits.insert(fruits.root, 3)

    print("Inorder traversal of the given tree")
    fruits.inorder(fruits.root)

    print("\nDelete 12")
    fruits.delete_node(fruits.root, 12)
    print("Inorder traversal of the modified tree")
    fruits.inorder(fruits.root)
