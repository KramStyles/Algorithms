class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(node_root, key):
    while node_root is not None:
        if key > node_root.data:
            node_root = node_root.right
        elif key < node_root.data:
            node_root = node_root.left
        else:
            return True
    return False


def insert(node, data):
    if not node.data:
        node = Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node


if __name__ == "__main__":
    root = Node(None)
    insert(root, 50)
    insert(root, 20)
    insert(root, 60)
    insert(root, 30)
    insert(root, 40)
    insert(root, 25)

    if search(root, 60):
        print("60 is available")
    else:
        print("60 is not available")
