# 树 (Tree) 数据结构

## 1. 基本概念

### 1.1 什么是树？

树是一种**非线性**的数据结构，它是由 n (n >= 0) 个节点组成的有限集合。

- 当 n = 0 时，称为空树
- 当 n > 0 时，有且仅有一个特定的节点称为**根节点 (Root)**
- 其余节点可分为 m (m >= 0) 个互不相交的有限集合，每个集合本身又是一棵树，称为根的**子树 (SubTree)**

### 1.2 基本术语

| 术语 | 说明 |
|------|------|
| **节点 (Node)** | 树中的每个元素 |
| **根节点 (Root)** | 树的顶层节点，没有父节点 |
| **父节点 (Parent)** | 某节点的上层节点 |
| **子节点 (Child)** | 某节点的下层节点 |
| **兄弟节点 (Sibling)** | 具有相同父节点的节点 |
| **叶子节点 (Leaf)** | 没有子节点的节点，也叫终端节点 |
| **内部节点** | 非叶子节点，也叫分支节点 |
| **边 (Edge)** | 连接两个节点的线段 |
| **路径 (Path)** | 从一个节点到另一个节点经过的边的序列 |
| **层 (Level)** | 根节点为第1层，根的子节点为第2层，以此类推 |
| **深度 (Depth)** | 从根节点到该节点的路径长度 |
| **高度 (Height)** | 从该节点到最远叶子节点的路径长度 |
| **度 (Degree)** | 节点拥有的子树数量 |
| **树的度** | 树中所有节点度的最大值 |

### 1.3 树的表示

```
        A          ← 根节点 (Level 1)
      / | \
     B  C  D       ← Level 2
    / \    |
   E   F   G       ← Level 3 (E, F, G 是叶子节点)
```

---

## 2. 二叉树 (Binary Tree)

### 2.1 定义

二叉树是每个节点**最多有两个子节点**的树结构，通常子树被称为"左子树"和"右子树"。

### 2.2 二叉树的性质

1. 第 i 层最多有 $2^{i-1}$ 个节点 (i >= 1)
2. 深度为 k 的二叉树最多有 $2^k - 1$ 个节点
3. 对于任意非空二叉树，若叶子节点数为 $n_0$，度为2的节点数为 $n_2$，则 $n_0 = n_2 + 1$

### 2.3 特殊的二叉树

#### 满二叉树 (Full Binary Tree)
- 所有叶子节点都在最后一层
- 每一层的节点数都达到最大值
- 节点总数: $2^k - 1$ (k 为深度)

```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

#### 完全二叉树 (Complete Binary Tree)
- 除最后一层外，每一层都是满的
- 最后一层的节点从左向右连续排列

```
        1
      /   \
     2     3
    / \   /
   4   5 6
```

#### 二叉搜索树 (Binary Search Tree, BST)
- 左子树所有节点的值 < 根节点的值
- 右子树所有节点的值 > 根节点的值
- 左右子树也分别是二叉搜索树

```
        8
      /   \
     3     10
    / \      \
   1   6     14
      / \   /
     4   7 13
```

#### 平衡二叉树 (AVL Tree)
- 任意节点的左右子树高度差不超过 1
- 保证查找效率为 O(log n)

#### 红黑树 (Red-Black Tree)
- 自平衡的二叉搜索树
- 每个节点有颜色属性（红或黑）
- 广泛应用于各种语言的标准库（如 Java TreeMap, C++ map）

---

## 3. Python 实现

### 3.1 二叉树节点定义

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 3.2 从列表构建二叉树

```python
from collections import deque
from typing import Optional, List

def build_tree(nums: List[Optional[int]]) -> Optional[TreeNode]:
    """从层序遍历列表构建二叉树"""
    if not nums or nums[0] is None:
        return None
    
    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nums):
        node = queue.popleft()
        
        # 左子节点
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        
        # 右子节点
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    
    return root

# 使用示例
# nums = [1, 2, 3, 4, 5, None, 6]
# root = build_tree(nums)
```

---

## 4. 树的遍历

### 4.1 深度优先遍历 (DFS)

#### 前序遍历 (Pre-order): 根 → 左 → 右

```python
def preorder_traversal(root: TreeNode) -> List[int]:
    """递归实现"""
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)  # 访问根
        dfs(node.left)           # 遍历左子树
        dfs(node.right)          # 遍历右子树
    dfs(root)
    return result

def preorder_iterative(root: TreeNode) -> List[int]:
    """迭代实现（使用栈）"""
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:  # 先右后左，因为栈是LIFO
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

#### 中序遍历 (In-order): 左 → 根 → 右

```python
def inorder_traversal(root: TreeNode) -> List[int]:
    """递归实现"""
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)           # 遍历左子树
        result.append(node.val)  # 访问根
        dfs(node.right)          # 遍历右子树
    dfs(root)
    return result

def inorder_iterative(root: TreeNode) -> List[int]:
    """迭代实现（使用栈）"""
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:              # 一直往左走
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right       # 转向右子树
    return result
```

**注意**: 对于二叉搜索树，中序遍历的结果是**有序**的！

#### 后序遍历 (Post-order): 左 → 右 → 根

```python
def postorder_traversal(root: TreeNode) -> List[int]:
    """递归实现"""
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)           # 遍历左子树
        dfs(node.right)          # 遍历右子树
        result.append(node.val)  # 访问根
    dfs(root)
    return result

def postorder_iterative(root: TreeNode) -> List[int]:
    """迭代实现"""
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]  # 反转结果
```

### 4.2 广度优先遍历 (BFS) / 层序遍历

```python
from collections import deque

def level_order(root: TreeNode) -> List[List[int]]:
    """层序遍历，返回每层的节点值"""
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

### 4.3 遍历方式对比

| 遍历方式 | 顺序 | 应用场景 |
|---------|------|---------|
| 前序遍历 | 根→左→右 | 复制树、表达式树的前缀表示 |
| 中序遍历 | 左→根→右 | BST 获取有序序列 |
| 后序遍历 | 左→右→根 | 删除树、计算目录大小 |
| 层序遍历 | 按层 | 按层打印、最短路径 |

---

## 5. 常见算法题型

### 5.1 求树的深度/高度

```python
def max_depth(root: TreeNode) -> int:
    """求二叉树的最大深度"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root: TreeNode) -> int:
    """求二叉树的最小深度"""
    if not root:
        return 0
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))
```

### 5.2 判断平衡二叉树

```python
def is_balanced(root: TreeNode) -> bool:
    """判断是否为平衡二叉树"""
    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
            return -1
        return 1 + max(left_h, right_h)
    
    return height(root) != -1
```

### 5.3 判断对称二叉树

```python
def is_symmetric(root: TreeNode) -> bool:
    """判断二叉树是否对称"""
    def check(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                check(left.left, right.right) and 
                check(left.right, right.left))
    
    return check(root, root) if root else True
```

### 5.4 翻转二叉树

```python
def invert_tree(root: TreeNode) -> TreeNode:
    """翻转二叉树"""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

### 5.5 最近公共祖先 (LCA)

```python
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """查找两个节点的最近公共祖先"""
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right
```

### 5.6 二叉树的路径和

```python
def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """判断是否存在路径和等于目标值"""
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return (has_path_sum(root.left, target_sum - root.val) or 
            has_path_sum(root.right, target_sum - root.val))

def path_sum(root: TreeNode, target_sum: int) -> List[List[int]]:
    """找出所有路径和等于目标值的路径"""
    result = []
    def dfs(node, path, remain):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and remain == node.val:
            result.append(path[:])
        dfs(node.left, path, remain - node.val)
        dfs(node.right, path, remain - node.val)
        path.pop()  # 回溯
    
    dfs(root, [], target_sum)
    return result
```

---

## 6. 二叉搜索树 (BST) 操作

### 6.1 查找

```python
def search_bst(root: TreeNode, val: int) -> TreeNode:
    """在BST中查找值"""
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)
```

### 6.2 插入

```python
def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    """向BST中插入值"""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root
```

### 6.3 删除

```python
def delete_node(root: TreeNode, key: int) -> TreeNode:
    """从BST中删除节点"""
    if not root:
        return None
    
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
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
        root.right = delete_node(root.right, min_node.val)
    
    return root
```

### 6.4 验证BST

```python
def is_valid_bst(root: TreeNode) -> bool:
    """验证是否为有效的BST"""
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

## 7. 其他重要的树结构

### 7.1 N叉树

```python
class NaryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []
```

### 7.2 字典树/前缀树 (Trie)

用于高效存储和检索字符串集合中的键。

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end
    
    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None
    
    def _find(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

### 7.3 堆 (Heap)

堆是一种特殊的完全二叉树，Python 中使用 `heapq` 模块。

```python
import heapq

# 最小堆
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
print(heapq.heappop(min_heap))  # 输出: 1

# 最大堆（取负值）
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))  # 输出: 3

# 从列表构建堆
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)  # 原地转换为堆
```

---

## 8. 时间复杂度总结

| 操作 | 普通二叉树 | BST (平均) | BST (最坏) | 平衡BST |
|------|-----------|-----------|-----------|---------|
| 查找 | O(n) | O(log n) | O(n) | O(log n) |
| 插入 | O(n) | O(log n) | O(n) | O(log n) |
| 删除 | O(n) | O(log n) | O(n) | O(log n) |
| 遍历 | O(n) | O(n) | O(n) | O(n) |

---

## 9. 刷题建议

1. **掌握递归思维**: 树的问题大多可以用递归解决，理解递归的三要素（终止条件、当前层操作、返回值）
2. **熟练遍历方式**: 四种遍历方式要能熟练写出递归和迭代版本
3. **分类练习**: 
   - 基础：遍历、深度、路径
   - 进阶：构建树、BST操作
   - 高级：LCA、序列化、Morris遍历
4. **画图辅助**: 做题时多画图，理清节点关系

---

## 10. LeetCode 推荐题目

| 难度 | 题号 | 题目 |
|-----|------|------|
| 简单 | 94 | 二叉树的中序遍历 |
| 简单 | 104 | 二叉树的最大深度 |
| 简单 | 101 | 对称二叉树 |
| 简单 | 226 | 翻转二叉树 |
| 简单 | 543 | 二叉树的直径 |
| 中等 | 102 | 二叉树的层序遍历 |
| 中等 | 98 | 验证二叉搜索树 |
| 中等 | 236 | 二叉树的最近公共祖先 |
| 中等 | 105 | 从前序与中序遍历序列构造二叉树 |
| 中等 | 114 | 二叉树展开为链表 |
| 中等 | 208 | 实现 Trie (前缀树) |
| 困难 | 124 | 二叉树中的最大路径和 |
| 困难 | 297 | 二叉树的序列化与反序列化 |
