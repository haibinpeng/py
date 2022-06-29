# 作者: Michael(phb)
# 2022年06月10日23时02分53秒
class Node:
    """结点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树"""

    def __init__(self):
        self.root = None
        self.queue = []  # 辅助队列

    def build_tree(self, element):
        """建树"""
        new_node = Node(element)  # 定义一个结点类的对象
        # 将新元素入队
        self.queue.append(new_node)
        # 将新结点放入树中
        # 如果树为空，新结点就是树根
        if self.root is None:
            self.root = new_node
        else:
            # 左子树为空，放左子树
            if self.queue[0].lchild is None:
                self.queue[0].lchild = new_node
            else:
                # 左子树不空，右子树为空，放右子树
                self.queue[0].rchild = new_node
                self.queue.pop(0)  # 放到右边后，队首元素要出队

    def preorder(self, node):
        """先序遍历"""
        if node:
            print(node.elem, end='')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def midorder(self, node):
        """中序遍历"""
        if node:
            self.preorder(node.lchild)
            print(node.elem, end='')
            self.preorder(node.rchild)

    def lastorder(self, node):
        self.preorder(node.lchild)
        self.preorder(node.rchild)
        print(node.elem, end='')


if __name__ == '__main__':
    T = Tree()
    for i in 'abcdefghij':
        T.build_tree(i)
    T.preorder(T.root)
    print()
    T.midorder(T.root)
    print()
    T.lastorder(T.root)
