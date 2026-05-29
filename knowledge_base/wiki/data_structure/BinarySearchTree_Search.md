# BinarySearchTree Search

## 核心概念

BST 查找从根结点开始。关键字小于当前结点则去左子树，大于则去右子树，等于则查找成功，遇空指针则失败。

## 考试识别信号

- 写 BST 查找路径。
- 判断关键字查找成功或失败。
- 比较 BST 查找和折半查找。

## 核心公式 / 代码模板

```cpp
BSTNode* SearchBST(BSTNode* root, int key) {
    while (root != nullptr) {
        if (key == root->data) return root;
        if (key < root->data) root = root->left;
        else root = root->right;
    }
    return nullptr;
}
```

## 手写步骤 / 计算步骤

1. 从根开始比较。
2. 小于当前结点走左子树。
3. 大于当前结点走右子树。
4. 记录访问过的结点。
5. 找到目标或遇空结束。

## 边界条件

空树查找失败。单结点树只比较一次。重复关键字按题目规则处理。

## 常见错误

- 误以为 BST 查找一定是 `O(log n)`。
- 比较方向写反。
- 忘记失败时停在空指针。
- 把 BST 和折半查找的存储要求混淆。

## 典型题型

- 写查找路径。
- 求查找比较次数。
- 判断插入序列形成的 BST 查找效率。

## 复杂度分析

树较平衡时平均约 `O(log n)`；退化为单链时最坏 `O(n)`。

## 与其他知识的联系

BST 查找依赖 [[BinarySearchTree_Basic]]。它与 [[Search_Basic]] 中折半查找都利用有序性，但存储结构不同。

## 相关链接

- [[BinarySearchTree_Basic]]
- [[Tree_Basic]]
- [[Search_Basic]]

## 待追问问题

- BST 查找失败路径如何确定？
- BST 平均查找长度如何计算？

## 来源

- knowledge_base/raw/data_structure/binary_search_tree_search.txt
