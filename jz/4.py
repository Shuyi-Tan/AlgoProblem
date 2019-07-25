class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstruct_binary_tree(pre, mid):
    if len(pre) < 1:
        return None
    head = Node(pre[0])
    index = mid.index(pre[0])
    head.left = reconstruct_binary_tree(pre[1:index+1], mid[:index])
    head.right = reconstruct_binary_tree(pre[index+1:], mid[index+1:])
    return head


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    mid = [4, 7, 2, 1, 5, 3, 8, 6]
    tree = reconstruct_binary_tree(pre, mid)
    print(tree.value)