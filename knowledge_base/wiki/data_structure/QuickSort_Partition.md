# QuickSort Partition

## 核心概念

快速排序通过 Partition 一趟划分确定一个枢轴 `pivot` 的最终位置。

划分结束后，`pivot` 左侧元素不大于它，右侧元素不小于它。

但一趟划分不会让整个序列完全有序，左右子区间仍需要继续递归排序。

## 核心代码模板

```cpp
int Partition(int a[], int low, int high) {
    int pivot = a[low];
    while (low < high) {
        while (low < high && a[high] >= pivot) --high;
        a[low] = a[high];
        while (low < high && a[low] <= pivot) ++low;
        a[high] = a[low];
    }
    a[low] = pivot;
    return low;
}

void QuickSort(int a[], int low, int high) {
    if (low >= high) return;

    int pivotPos = Partition(a, low, high);
    QuickSort(a, low, pivotPos - 1);
    QuickSort(a, pivotPos + 1, high);
}
```

## 手写步骤

1. 确认待划分区间非空，满足 `low <= high`。
2. 保存 `pivot = a[low]`。
3. 从右侧找小于 pivot 的元素，填到左侧坑位。
4. 从左侧找大于 pivot 的元素，填到右侧坑位。
5. 重复直到 `low == high`。
6. 把 pivot 放回 `a[low]`。
7. 返回 pivot 的最终位置。
8. 对左右子区间递归快速排序。

## 常见错误

- 忘记保存 pivot，导致枢轴值被覆盖。
- high 和 low 移动顺序写错。
- 递归边界写成包含 pivot，导致死递归。
- 误以为一趟划分后整个序列已经有序。
- 对空区间调用 Partition。

## 典型题型

- 写出快速排序一趟划分过程。
- 给定序列，求 Partition 后 pivot 的位置。
- 补全快速排序递归代码。
- 判断一趟划分后的序列是否可能正确。
- 分析快速排序递归边界。

## 复杂度分析

Partition 一趟划分的时间复杂度是 O(n)。

快速排序平均时间复杂度通常是 O(n log n)。

快速排序最坏时间复杂度可能退化到 O(n^2)。

递归会带来额外栈空间，空间复杂度与递归深度有关。

## 与其他知识的联系

快速排序属于基础排序。

Partition 使用顺序表下标移动和元素覆盖思想。

它和插入排序、选择排序、冒泡排序一样，常用于比较排序复杂度和稳定性。

## 相关链接

- [[QuickSort_Partition]]
- [[Sort_Basic]]
- [[DataStructure_Code_Templates]]
- [[DataStructure_Problem_Patterns]]
- [[SeqList_Insert_Delete]]

## 待追问问题

- 为什么不同教材的 Partition 模板移动顺序可能不同？
- 快速排序是否稳定？
- pivot 选择策略会如何影响复杂度？

## 来源

- knowledge_base/raw/data_structure/quick_sort_partition.txt
