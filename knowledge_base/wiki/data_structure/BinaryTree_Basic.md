# BinaryTree Basic

## 核心概念

二叉树是每个结点最多有两个孩子的树形结构。

一个非空二叉树由根结点、左子树和右子树组成。

二叉树适合表达层次关系和递归结构。

## 核心代码模板

```cpp
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
};

void preorder(TreeNode* root) {
    if (root == nullptr) return;
    visit(root);
    preorder(root->left);
    preorder(root->right);
}

void inorder(TreeNode* root) {
    if (root == nullptr) return;
    inorder(root->left);
    visit(root);
    inorder(root->right);
}

void postorder(TreeNode* root) {
    if (root == nullptr) return;
    postorder(root->left);
    postorder(root->right);
    visit(root);
}
```

## 手写步骤

前序遍历：根，左，右。

中序遍历：左，根，右。

后序遍历：左，右，根。

层次遍历：按层访问，通常使用队列。

还原二叉树：

1. 前序或后序确定根结点。
2. 中序把结点划分为左子树和右子树。
3. 对左右子树递归处理。

## 常见错误

- 把树的度和结点的度混淆。
- 认为只有前序和后序就能唯一还原普通二叉树。
- 完全二叉树编号公式从 0 开始和从 1 开始混用。
- 滥用 `n0 = n2 + 1`，没有说明它适用于非空二叉树。
- 层次遍历不用队列导致顺序错误。

## 典型题型

- 根据遍历序列还原二叉树。
- 写出前序、中序、后序、层次遍历结果。
- 使用完全二叉树编号求父结点或孩子结点。
- 根据 `n0 = n2 + 1` 求叶子结点数。

## 复杂度分析

遍历整棵二叉树的时间复杂度为 O(n)。

递归遍历的额外空间与树高有关。

层次遍历需要队列，额外空间与某一层最大结点数有关。

## 与其他知识的联系

二叉树遍历会用到递归、栈和队列。

二叉搜索树、堆、哈夫曼树都建立在二叉树基础上。

## Obsidian 风格相关链接

- [[BinaryTree_Basic]]
- [[Stack_Queue_Basic]]
- [[Search_Basic]]
- [[Sort_Basic]]

## 待追问问题

- 满二叉树、完全二叉树、平衡二叉树如何区分？
- 二叉树顺序存储适合什么树形？

## 来源

- knowledge_base/raw/data_structure/binary_tree_basic.txt
