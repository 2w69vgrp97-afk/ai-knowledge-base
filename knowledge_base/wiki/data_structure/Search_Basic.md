# Search Basic

## 核心概念

查找是在数据集合中寻找目标元素。

查找效率取决于数据是否有序、存储结构是否支持快速定位，以及算法本身的比较策略。

## 核心代码模板

```cpp
int sequentialSearch(const int a[], int n, int key) {
    for (int i = 0; i < n; ++i) {
        if (a[i] == key) return i;
    }
    return -1;
}

int binarySearch(const int a[], int n, int key) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```

## 手写步骤

顺序查找：

1. 从第一个元素开始。
2. 逐个比较关键字。
3. 找到则返回位置。
4. 扫描结束仍未找到则查找失败。

折半查找：

1. 设置查找区间。
2. 取中间位置。
3. 比较目标和中间元素。
4. 根据有序性缩小一半区间。
5. 区间为空则查找失败。

## 常见错误

- 对无序表使用折半查找。
- 在普通单链表中直接套用折半查找。
- 更新 `low` 和 `high` 时没有排除 `mid`，导致死循环。
- 忘记查找失败条件。

## 典型题型

- 写顺序查找和折半查找过程。
- 给出折半查找的比较序列。
- 画折半查找判定树。
- 计算平均查找长度 ASL。

## 复杂度分析

顺序查找：时间复杂度 O(n)。

折半查找：时间复杂度 O(log n)。

折半查找要求表有序，并且支持按下标随机访问。

## 与其他知识的联系

折半查找依赖顺序表的随机访问能力。

树形查找结构可以看作把比较过程组织成层次结构。

排序可以为高效查找创造有序前提。

## Obsidian 风格相关链接

- [[Search_Basic]]
- [[Sort_Basic]]
- [[SeqList_Insert_Delete]]
- [[BinaryTree_Basic]]

## 待追问问题

- ASL 的计算公式如何从判定树理解？
- 动态数据频繁插入删除时，是否值得维持有序表？

## 来源

- knowledge_base/raw/data_structure/search_basic.txt
