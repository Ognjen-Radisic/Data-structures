class Node:
    def __init__(self, value= None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, number):
        if self.root == None:
            self.root = Node(number)
        else:
            self._insert(self.root, number)
    
    def _insert(self, cur_node, value):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(cur_node.left_child, value)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(cur_node.right_child, value)
        else:
            print("This element already exist in the tree")

    def print_tree(self):
        if self.root == None:
            print("empty tree")
            return
        else:
            self._print_t(self.root)
    
    def _print_t(self, cur_node):
        if cur_node.left_child != None:
            self._print_t(cur_node.left_child)
        print(cur_node.value)
        if cur_node.right_child != None:
            self._print_t(cur_node.right_child)
    
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_num):
        if cur_node == None: return cur_num
        left_max = self._height(cur_node.left_child, cur_num+1)
        right_max = self._height(cur_node.right_child, cur_num+1)
        return max(left_max, right_max)

    def search(self, value):
        if self.root == None:
            return False
        else:
            return self._search(self.root, value)
    
    def _search(self, cur_node, value):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(cur_node.left_child, value)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(cur_node.right_child, value)
        return False

#testing

def number_filler(tree, num_elem= 100, max_elem= 1000):
    import random
    for number in range(num_elem):
        cur = random.randint(0, max_elem)
        tree.insert(cur)
    return tree

tree = BinaryTree()
tree = number_filler(tree)
tree.insert(958)
tree.print_tree()
print("Tree height is:",tree.height())
print("Is given element in the tree?", tree.search(959))