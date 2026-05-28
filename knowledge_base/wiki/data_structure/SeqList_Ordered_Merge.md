# SeqList Ordered Merge

## 核心概念

有序顺序表合并是把两个已经有序的顺序表合成为一个新的有序顺序表。

它利用输入表已经有序的前提，用线性扫描完成合并。

## 核心代码模板

```cpp
struct SeqList {
    int data[1000];
    int length = 0;
};

bool mergeOrdered(const SeqList& a, const SeqList& b, SeqList& c) {
    if (a.length + b.length > 1000) return false;

    int i = 0;
    int j = 0;
    int k = 0;

    while (i < a.length && j < b.length) {
        if (a.data[i] <= b.data[j]) {
            c.data[k++] = a.data[i++];
        } else {
            c.data[k++] = b.data[j++];
        }
    }

    while (i < a.length) c.data[k++] = a.data[i++];
    while (j < b.length) c.data[k++] = b.data[j++];

    c.length = k;
    return true;
}
```

## 手写步骤

1. 用 `i` 指向第一个表。
2. 用 `j` 指向第二个表。
3. 用 `k` 指向结果表写入位置。
4. 比较当前两个元素，把较小者写入结果表。
5. 对应下标后移。
6. 某个表扫描完后，把另一个表剩余元素复制到结果表。

## 常见错误

- 忽略结果表容量。
- 两个表有相等元素时破坏稳定性。
- 一个表扫描结束后忘记复制剩余元素。
- 输入表无序却使用有序合并方法。

## 典型题型

- 合并两个递增顺序表。
- 要求合并后仍然递增。
- 分析合并过程的比较次数和时间复杂度。
- 讨论一个表为空或两个表都为空的情况。

## 复杂度分析

时间复杂度：O(m + n)。

额外空间复杂度：如果使用新结果表，为 O(m + n)。

若只分析除结果表外的辅助变量，额外变量为 O(1)。

## 与其他知识的联系

有序合并是归并排序的基础步骤。

它和顺序表连续扫描、排序稳定性有关。

## Obsidian 风格相关链接

- [[SeqList_Ordered_Merge]]
- [[SeqList_Insert_Delete]]
- [[Sort_Basic]]

## 待追问问题

- 有序合并是否可以原地完成？
- 合并链表和合并顺序表有什么不同？

## 来源

- knowledge_base/raw/data_structure/seq_list_ordered_merge.txt
