# models.py
class Node:
    def create(value):
        node = Node()
        node.value = value
        node.left = None
        node.right = None
        node.height = 1
        node.expanded = False
        return node


class AVLTree:
    def height(n):
        return n.height if n else 0

    def update_height(n):
        n.height = max(AVLTree.height(n.left), AVLTree.height(n.right)) + 1

    def balance_factor(n):
        return AVLTree.height(n.left) - AVLTree.height(n.right)

    def rotate_right(y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        AVLTree.update_height(y)
        AVLTree.update_height(x)
        return x

    def rotate_left(x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        AVLTree.update_height(x)
        AVLTree.update_height(y)
        return y

    def insert(node, value):
        if not node:
            return Node.create(value)

        if value < node.value:
            node.left = AVLTree.insert(node.left, value)
        else:
            node.right = AVLTree.insert(node.right, value)

        AVLTree.update_height(node)
        balance = AVLTree.balance_factor(node)

        if balance > 1 and value < node.left.value:
            return AVLTree.rotate_right(node)
        if balance < -1 and value > node.right.value:
            return AVLTree.rotate_left(node)
        if balance > 1 and value > node.left.value:
            node.left = AVLTree.rotate_left(node.left)
            return AVLTree.rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = AVLTree.rotate_right(node.right)
            return AVLTree.rotate_left(node)

        return node

    def get_min(node):
        while node.left:
            node = node.left
        return node

    def delete(node, value):
        if not node:
            return node

        if value < node.value:
            node.left = AVLTree.delete(node.left, value)
        elif value > node.value:
            node.right = AVLTree.delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = AVLTree.get_min(node.right)
            node.value = temp.value
            node.right = AVLTree.delete(node.right, temp.value)

        AVLTree.update_height(node)
        balance = AVLTree.balance_factor(node)

        if balance > 1 and AVLTree.balance_factor(node.left) >= 0:
            return AVLTree.rotate_right(node)
        if balance > 1 and AVLTree.balance_factor(node.left) < 0:
            node.left = AVLTree.rotate_left(node.left)
            return AVLTree.rotate_right(node)
        if balance < -1 and AVLTree.balance_factor(node.right) <= 0:
            return AVLTree.rotate_left(node)
        if balance < -1 and AVLTree.balance_factor(node.right) > 0:
            node.right = AVLTree.rotate_right(node.right)
            return AVLTree.rotate_left(node)

        return node