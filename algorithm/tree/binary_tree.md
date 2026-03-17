# 二叉树 (Binary Tree)

## 1. 基本概念

### 1.1 什么是二叉树

二叉树是一种树形数据结构，其中每个节点最多有两个子节点，分别称为**左子节点**和**右子节点**。

```
        1          <- 根节点 (root)
       / \
      2   3        <- 子节点
     / \   \
    4   5   6      <- 叶子节点 (没有子节点的节点)
```

### 1.2 基本术语

| 术语 | 说明 |
|------|------|
| **节点 (Node)** | 树中的每个元素 |
| **根节点 (Root)** | 树的顶部节点，没有父节点 |
| **叶子节点 (Leaf)** | 没有子节点的节点 |
| **父节点 (Parent)** | 有子节点的节点 |
| **子节点 (Child)** | 某节点的下级节点 |
| **兄弟节点 (Sibling)** | 拥有相同父节点的节点 |
| **深度 (Depth)** | 从根节点到该节点的边数 |
| **高度 (Height)** | 从该节点到最远叶子节点的边数 |
| **层 (Level)** | 根节点为第1层，依次递增 |

---

## 2. 二叉树的类型

### 2.1 满二叉树 (Full Binary Tree)
每个节点要么有 0 个子节点，要么有 2 个子节点。

```
        1
       / \
      2   3
     / \
    4   5
```

### 2.2 完全二叉树 (Complete Binary Tree)
除最后一层外，所有层都被完全填满，且最后一层的节点从左到右连续排列。

```
        1
       / \
      2   3
     / \  /
    4  5 6
```

### 2.3 完美二叉树 (Perfect Binary Tree)
所有内部节点都有两个子节点，所有叶子节点在同一层。

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

### 2.4 二叉搜索树 (Binary Search Tree, BST)
- 左子树所有节点的值 < 根节点的值
- 右子树所有节点的值 > 根节点的值
- 左右子树也都是二叉搜索树

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

### 2.5 平衡二叉树 (Balanced Binary Tree)
任意节点的左右子树高度差不超过 1。常见的有：
- **AVL 树**
- **红黑树**

---

## 3. 二叉树的 Python 实现

### 3.1 节点定义

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 3.2 构建二叉树

```python
# 手动构建
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 从列表构建（层序）
from collections import deque

def build_tree(values):
    """从列表构建二叉树（层序遍历顺序，None 表示空节点）"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # 左子节点
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # 右子节点
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# 使用示例
root = build_tree([1, 2, 3, 4, 5, None, 6])
```

### 3.3 使用数组构建
- 索引为i，左子节点为: 2 * i + 1，右子节点为：2 * i + 2
    - (i << 2) + 1, (i << 2) + 2
- 父节点：(i - 1) // 2   向下取整 
    - (i - 1) >> 2

---

## 4. 二叉树的遍历

### 4.1 深度优先遍历 (DFS)

#### 前序遍历 (Preorder): 根 → 左 → 右

```python
# 递归实现
def preorder_recursive(root):
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)

# 迭代实现
def preorder_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        # 先压右子节点，再压左子节点（栈是后进先出）
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

#### 中序遍历 (Inorder): 左 → 根 → 右

```python
# 递归实现
def inorder_recursive(root):
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

# 迭代实现
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        # 一直往左走
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result
```

#### 后序遍历 (Postorder): 左 → 右 → 根

```python
# 递归实现
def postorder_recursive(root):
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]

# 迭代实现
def postorder_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        # 先压左子节点，再压右子节点
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result[::-1]  # 反转结果
```

### 4.2 广度优先遍历 (BFS) / 层序遍历

```python
from collections import deque

def level_order(root):
    """层序遍历，返回二维数组"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### 4.3 遍历对比

```
        1
       / \
      2   3
     / \
    4   5

前序遍历: [1, 2, 4, 5, 3]  (根左右)
中序遍历: [4, 2, 5, 1, 3]  (左根右)
后序遍历: [4, 5, 2, 3, 1]  (左右根)
层序遍历: [[1], [2, 3], [4, 5]]
```

---

## 5. 常见操作

### 5.1 计算树的高度/深度

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 5.2 计算节点数量

```python
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### 5.3 判断是否为平衡二叉树

```python
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        
        left_height = check(node.left)
        right_height = check(node.right)
        
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    return check(root) != -1
```

### 5.4 判断是否为对称二叉树

```python
def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return is_mirror(root, root) if root else True
```

### 5.5 翻转二叉树

```python
def invert_tree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root
```

### 5.6 查找最近公共祖先 (LCA)

```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right
```

---

## 6. 二叉搜索树 (BST) 操作

### 6.1 搜索

```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
```

### 6.2 插入

```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    
    return root
```

### 6.3 删除

```python
def delete_bst(root, key):
    if not root:
        return None
    
    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        # 找到要删除的节点
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # 有两个子节点：找右子树的最小值替换
        min_node = root.right
        while min_node.left:
            min_node = min_node.left
        root.val = min_node.val
        root.right = delete_bst(root.right, min_node.val)
    
    return root
```

### 6.4 验证 BST

```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))
```

---

## 7. 经典算法题目

| 题目 | 难度 | 考察点 |
|------|------|--------|
| 二叉树的最大深度 | 简单 | 递归/DFS |
| 验证二叉搜索树 | 中等 | 中序遍历/递归 |
| 二叉树的层序遍历 | 中等 | BFS |
| 从前序与中序遍历序列构造二叉树 | 中等 | 递归/分治 |
| 二叉树的最近公共祖先 | 中等 | 递归 |
| 二叉树中的最大路径和 | 困难 | DFS/动态规划思想 |
| 序列化和反序列化二叉树 | 困难 | BFS/DFS |

---

## 8. 时间/空间复杂度

| 操作 | 平均时间复杂度 | 最坏时间复杂度 | 空间复杂度 |
|------|---------------|---------------|-----------|
| 搜索 (BST) | O(log n) | O(n) | O(h) |
| 插入 (BST) | O(log n) | O(n) | O(h) |
| 删除 (BST) | O(log n) | O(n) | O(h) |
| 遍历 | O(n) | O(n) | O(h) |

> **注**: h 为树的高度，平衡树 h = log(n)，最坏情况（链状）h = n

---

## 9. 学习建议

1. **先掌握遍历**: 前序、中序、后序、层序遍历是基础
2. **理解递归思想**: 二叉树问题大多可以用递归解决
3. **画图分析**: 遇到复杂问题先画图理清思路
4. **多练习**: LeetCode 上有大量二叉树相关题目
5. **注意边界条件**: 空树、单节点、只有左/右子树等情况
