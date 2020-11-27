class BST:

    def __init__(self, key):
        self.key = key
        self.root = None

    class Node:
        def __init__(self, data, key_, parent):
            self.parent = parent
            self.key = key_
            self.data = data
            self.left_child = None
            self.right_child = None

    def add(self, data):
        current = self.root

        if self.root is None:
            self.root = self.Node(data, self.key(data), None);
            return

        while True:
            if self.key(current.data) < self.key(data):
                if current.right_child is None:
                    current.right_child = self.Node(data, self.key(data), parent=current);
                    return
                else:
                    current = current.right_child
            elif self.key(current.data) > self.key(data):
                if current.left_child is None:
                    current.left_child = self.Node(data, self.key(data), parent=current);
                    return
                else:
                    current = current.left_child
            else:
                current.data = data;return

    def limit_element(self, key):
        if self.root is not None:
            current = self.root
            while key(current) is not None:
                current = key(current)
            return current

    def get_min_element(self):
        return self.limit_element(lambda x: x.left_child).data

    def get_max_element(self):
        return self.limit_element(lambda x: x.right_child).data

    def remove_element(self, node):
        if node.right_child is not None:
            if node.parent is None:
                node.right_child.parent = None
                self.root = node.right_child
            else:
                node.parent.left_child = node.right_child
        else:
            if node.parent is not None:
                node.parent.left_child = None
            else:
                self.root = None

    def remove_min_element(self):
        self.remove_element(self.limit_element(lambda x: x.left_child))
