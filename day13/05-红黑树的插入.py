# 作者: Michael(phb)
# 2022年06月13日23时00分21秒
RED = 0
BLACK = 1


class RedBlackTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None  # 指向父结点
        self.color = RED


def left_rotate(tree, node: RedBlackTreeNode):
    """左旋"""
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p
    if not node.p:
        tree.root = node_right
    elif node == node.p.left:
        node.p.left = node_right
    else:
        node.p.right = node_right
    if node_right.left:
        node_right.left.p = node
    node.right = node_right.left
    node.p = node_right
    node_right.left = node


def right_rotate(tree, node: RedBlackTreeNode):
    """右旋"""
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p
    if not node.p:
        tree.root = node_left
    elif node == node.p.left:
        node.p.left = node_left
    elif node == node.p.right:
        node.p.right = node_left
    if node_left.right:
        node_left.right.p = node
    node.left = node_left.right
    node.p = node_left
    node_left.right = node


def rbtree_print(node, key, direction):
    """打印红黑树"""
    if node:
        if direction == 0:  # 根结点
            print('%2d(B) is root' % node.value)
        else:  # 分支结点
            print("%2d(%s) is %2d's %6s child"
                  % (node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")))
        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


class RedBlackTree:
    def __init__(self):
        self.root: RedBlackTreeNode = None

    def __insert_fixup(self, node):
        parent: RedBlackTreeNode = node.p
        while parent and parent.color == RED:
            grandparent: RedBlackTreeNode = parent.p
            if parent is grandparent.left:
                uncle: RedBlackTreeNode = grandparent.right
                if uncle and uncle.color == RED:  # 情形三
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                    parent = node.p
                    continue
                if node is parent.right:  # 情形四
                    left_rotate(self, parent)
                    parent, node = node, parent  # 转换为情形五
                # 情形五
                right_rotate(self, grandparent)
                parent.color = BLACK
                grandparent.color = RED
            else:
                # 对称过去
                uncle: RedBlackTreeNode = grandparent.left
                if uncle and uncle.color == RED:  # 情形三
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                    parent = node.p
                    continue
                if node is parent.left:  # 情形四
                    right_rotate(self, parent)
                    parent, node = node, parent  # 转换为情形五
                # 情形五
                left_rotate(self, grandparent)
                parent.color = BLACK
                grandparent.color = RED
        self.root.color = BLACK

    def insert(self, node: RedBlackTreeNode):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node:
                parent = current_node
                if current_node.value > node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            node.p = parent
            if parent.value > node.value:
                parent.left = node
            else:
                parent.right = node
        self.__insert_fixup(node)


def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RedBlackTree()
    for number in number_list:
        node = RedBlackTreeNode(number)
        tree.insert(node)
    rbtree_print(tree.root, 0, 0)


if __name__ == '__main__':
    main()
