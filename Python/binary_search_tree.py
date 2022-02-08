class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, key):
    while root is not None:
        if key > root.data:
            root = root.right
        elif key < root.data:
            root = root.left
        else:
            return True
    return False


def insert(Node, data):
    if not Node:
        return NewNode(data)
    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)
    return Node


if __name__ == '__main__':
    root = None
    insert(root, 50)
    insert(root, 20)
    insert(root, 60)
    insert(root, 30)
    insert(root, 40)
    insert(root, 25)

    if search(root, 60):
        print('60 is available')
    else:
        print('60 is not available')
