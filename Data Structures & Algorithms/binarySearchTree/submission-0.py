class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    """
                5
        3           8
    2       4           9
1

    """
    
    def __init__(self):
        self.head = None


    def insert(self, key: int, val: int) -> None:
        if self.head == None:
            self.head = TreeNode(key, val)
            return
        curr = self.head
        while True:
            if key < curr.key:
                if curr.left == None:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right == None:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
            else: # key == curr.key:
                curr.val = val
                return


    def get(self, key: int) -> int:
        curr = self.head
        while True:
            if curr == None: 
                return -1
            elif key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else: # key == curr.key:
                return curr.val

    def getMin(self) -> int:
        if self.head == None:
            return -1
        curr = self.head
        while True:
            if curr.left == None: 
                return curr.val
            curr = curr.left
            
        


    def getMax(self) -> int:
        if self.head == None:
            return -1
        curr = self.head
        while True:
            if curr.right == None: 
                return curr.val
            curr = curr.right


    def remove(self, key: int) -> None:
        self.head = self._remove(self.head, key)

    def _findMinNode(self, node):
        while node and node.left:
            node = node.left
        return node

    def _remove(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # two children
            succ = self._findMinNode(node.right)
            node.key, node.val = succ.key, succ.val
            node.right = self._remove(node.right, succ.key)

        return node


    def getInorderKeys(self) -> List[int]:

        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.key)
            dfs(node.right)
        dfs(self.head)
        return result


