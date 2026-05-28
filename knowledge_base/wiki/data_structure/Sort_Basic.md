# Sort Basic

## 核心概念

排序是把数据按照关键字顺序重新排列。

排序不仅比较速度，还要比较空间复杂度、稳定性，以及最好、平均、最坏情况。

## 核心代码模板

```cpp
void insertionSort(int a[], int n) {
    for (int i = 1; i < n; ++i) {
        int value = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > value) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = value;
    }
}

void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (a[j] < a[minIndex]) minIndex = j;
        }
        int temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
}
```

## 手写步骤

直接插入排序：

1. 前面部分视为有序。
2. 取当前元素。
3. 在有序部分中向前比较并移动元素。
4. 把当前元素插入正确位置。

简单选择排序：

1. 在未排序部分选择最小元素。
2. 与未排序部分第一个元素交换。
3. 重复直到全部有序。

归并排序：

1. 先分解序列。
2. 再合并有序子序列。

快速排序：

1. 通过 [[QuickSort_Partition|Partition]] 一趟划分确定枢轴位置。
2. 再递归处理枢轴左右两侧子区间。

## 常见错误

- 只比较时间复杂度，忽略稳定性和空间复杂度。
- 把简单选择排序误认为稳定排序。
- 归并排序时忘记需要额外空间。
- 插入排序中移动方向写反。
- 误以为快速排序一趟划分后整个序列已经有序。

## 典型题型

- 给出某种排序每一趟后的序列。
- 判断排序算法是否稳定。
- 比较最好、平均、最坏时间复杂度。
- 根据数据特点选择排序方法。

## 复杂度分析

直接插入排序：最好 O(n)，平均和最坏 O(n^2)，通常稳定。

简单选择排序：通常 O(n^2)，一般不稳定，交换次数较少。

归并排序：时间复杂度通常 O(n log n)，通常需要额外空间。

快速排序：平均时间复杂度通常 O(n log n)，最坏情况可能退化到 O(n^2)。

## 与其他知识的联系

插入排序和顺序表插入有关。

归并排序依赖有序顺序表合并。

排序可以提升后续查找效率。

## Obsidian 风格相关链接

- [[Sort_Basic]]
- [[Search_Basic]]
- [[SeqList_Ordered_Merge]]
- [[SeqList_Insert_Delete]]
- [[QuickSort_Partition]]

## 待追问问题

- 冒泡排序、快速排序、堆排序的复杂度和稳定性如何比较？
- 内部排序和外部排序的区别是什么？

## 来源

- knowledge_base/raw/data_structure/sort_basic.txt
