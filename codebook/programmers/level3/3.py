import sys
sys.setrecursionlimit(100000)

# 길찾기 게임
class Node:
    def __init__(self, x, index):
        self.value = x
        self.index = index
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, x, index):
        self.value = x
        self.index = index
        self.current_node = self.root
        while True:
            if self.value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(self.value, self.index)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(self.value, self.index)
                    break
    
    def pre_order_traversal(self):
        pre_stack = []
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                pre_stack.append(root.index)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
        return pre_stack

    def post_order_traversal(self):
        post_stack = []
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                post_stack.append(root.index)
        _post_order_traversal(self.root)
        return post_stack

def solution(nodeinfo):
    
    index_nodes = [[i+1, nodeinfo[i][0], nodeinfo[i][1]] for i in range(len(nodeinfo))]
    nodes = sorted(index_nodes, key = lambda x : -int(x[2]))

    root = Node(nodes[0][1], nodes[0][0])
    bst = BST(root)
    for node in nodes[1:]: bst.insert(node[1], node[0])
    
    ans = []
    ans.append(bst.pre_order_traversal())
    ans.append(bst.post_order_traversal())

    return ans


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))

# 이진트리를 구성하자.
# X값을 value로 해서 이진트리를 만들면 될 것 같음.