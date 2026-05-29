# BinarySearchTree Basic

## 核心概念

二叉排序树又称二叉搜索树 BST。对任意结点，左子树所有关键字小于根，右子树所有关键字大于根，左右子树也分别是二叉排序树。

BST 的中序遍历得到递增序列。若允许重复关键字，重复元素放左侧还是右侧必须按题目约定。

## 考试识别信号

- 构造二叉排序树。
- 判断中序遍历结果。
- 写查找、插入或删除过程。

## 核心公式 / 代码模板

```cpp
BSTNode* Search(BSTNode* root, int key) {
    while (root != nullptr) {
        if (key == root->data) return root;
        if (key < root->data) root = root->left;
        else root = root->right;
    }
    return nullptr;
}
```

删除基础思想：

- 叶子结点：直接删除。
- 只有一个子树：用子树替代。
- 有两个子树：用中序前驱或中序后继替代，再删除原前驱或后继结点。

## 手写步骤 / 计算步骤

1. 从根开始比较。
2. 小于当前结点走左子树，大于走右子树。
3. 查找遇空失败。
4. 插入时把新结点接到第一次遇到的空位置。
5. 删除时按孩子个数分类处理。

## 边界条件

空树查找失败，插入时新结点成为根。单结点树删除后变为空树。

## 常见错误

- 忘记 BST 中序遍历递增。
- 误以为 BST 一定平衡。
- 删除有两个孩子的结点后破坏 BST 性质。
- 未按题目处理重复关键字。

## 典型题型

- 给序列构造 BST。
- 写查找路径。
- 删除指定结点后画新树。

## 复杂度分析

树较平衡时，查找、插入、删除约为 `O(log n)`。退化为单链时，最坏为 `O(n)`。

## 与其他知识的联系

BST 查找与 [[BinarySearchTree_Search]] 直接相关。BST 的中序遍历依赖 [[BinaryTree_Basic]]。

## 相关链接

- [[Tree_Basic]]
- [[BinaryTree_Basic]]
- [[BinarySearchTree_Search]]
- [[Search_Basic]]

## 待追问问题

- BST 删除有两个孩子的结点时，前驱和后继如何选择？
- 平衡二叉树如何避免 BST 退化？

## 来源

- knowledge_base/raw/data_structure/binary_search_tree_basic.txt
