# Shell Sort Basic

## 核心概念

希尔排序又称缩小增量排序。它按增量 `gap` 将序列分组，对每组做插入排序，再逐步缩小 `gap`，直到 `gap = 1`。

希尔排序不稳定，时间复杂度与增量序列有关。

## 考试识别信号

- 题目给出增量序列。
- 要求写某一趟希尔排序结果。
- 判断稳定性或复杂度。

## 核心公式 / 代码模板

```cpp
void ShellSort(int a[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; ++i) {
            int x = a[i];
            int j = i - gap;
            while (j >= 0 && a[j] > x) {
                a[j + gap] = a[j];
                j -= gap;
            }
            a[j + gap] = x;
        }
    }
}
```

## 手写步骤 / 计算步骤

1. 按给定 `gap` 分组。
2. 每组做直接插入排序。
3. 缩小 `gap`。
4. 重复直到 `gap = 1`。

## 边界条件

空表或单元素表已有序。增量序列最终必须到 1。

## 常见错误

- 忘记最后增量必须为 1。
- 把希尔排序误认为稳定。
- 分组时没有按 `gap` 间隔取元素。
- 把复杂度写成固定值，忽略增量序列。

## 典型题型

- 给定增量序列，写每趟结果。
- 判断希尔排序是否稳定。
- 比较希尔排序和直接插入排序。

## 复杂度分析

时间复杂度与增量序列有关。空间复杂度通常为 `O(1)`。希尔排序不稳定。

## 与其他知识的联系

希尔排序是插入排序的改进，关联 [[Sort_Basic]] 和 [[Sort_Complexity_Stability_Summary]]。

## 相关链接

- [[Sort_Basic]]
- [[Binary_Insertion_Sort]]
- [[Sort_Complexity_Stability_Summary]]

## 待追问问题

- 常见教材采用哪种希尔增量序列？
- 为什么希尔排序不稳定？

## 来源

- knowledge_base/raw/data_structure/shell_sort_basic.txt
