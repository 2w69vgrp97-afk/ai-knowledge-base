# Heap Sort Basic

## 核心概念

堆是满足特定次序关系的完全二叉树。大根堆中每个结点关键字大于等于孩子关键字；小根堆中每个结点关键字小于等于孩子关键字。

堆排序通常用大根堆得到递增序列。堆排序不稳定，时间复杂度为 `O(n log n)`。

## 考试识别信号

- 判断序列是否为堆。
- 建大根堆或小根堆。
- 写堆排序某一趟结果。

## 核心公式 / 代码模板

0-based 数组表示堆：

- 左孩子：`2 * i + 1`
- 右孩子：`2 * i + 2`
- 父结点：`(i - 1) / 2`

```cpp
void SiftDown(int a[], int start, int end) {
    int i = start;
    int x = a[i];
    int child = 2 * i + 1;
    while (child <= end) {
        if (child + 1 <= end && a[child + 1] > a[child]) ++child;
        if (a[child] <= x) break;
        a[i] = a[child];
        i = child;
        child = 2 * i + 1;
    }
    a[i] = x;
}
```

## 手写步骤 / 计算步骤

1. 从最后一个非叶子结点开始向下调整，建立初始堆。
2. 交换堆顶和堆尾。
3. 堆长度减一。
4. 对新堆顶向下调整。
5. 重复直到只剩一个元素。

## 边界条件

空表或单元素表已有序。1-based 数组公式不同，考试按题目编号约定。

## 常见错误

- 忘记堆必须是完全二叉树。
- 把堆误认为完全有序序列。
- 建堆时从叶子开始做无意义调整。
- 认为堆排序稳定。

## 典型题型

- 判断是否为大根堆或小根堆。
- 手写建堆过程。
- 写堆排序交换与调整后的序列。

## 复杂度分析

建堆为 `O(n)`，堆排序整体为 `O(n log n)`。空间复杂度为 `O(1)`。不稳定。

## 与其他知识的联系

堆是完全二叉树的应用，关联 [[BinaryTree_Basic]]、[[Sort_Complexity_Stability_Summary]]。

## 相关链接

- [[BinaryTree_Basic]]
- [[Sort_Basic]]
- [[Sort_Complexity_Stability_Summary]]

## 待追问问题

- 1-based 堆数组下标公式如何写？
- 为什么建堆是 `O(n)`？

## 来源

- knowledge_base/raw/data_structure/heap_sort_basic.txt
