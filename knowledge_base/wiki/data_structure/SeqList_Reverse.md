# SeqList Reverse

## 核心概念

顺序表逆置是在原表中把元素顺序反过来。

核心思想是使用左右两个下标，从两端向中间交换元素。

## 核心代码模板

```cpp
struct SeqList {
    int data[1000];
    int length = 0;
};

void reverse(SeqList& list) {
    int low = 0;
    int high = list.length - 1;

    while (low < high) {
        int temp = list.data[low];
        list.data[low] = list.data[high];
        list.data[high] = temp;
        ++low;
        --high;
    }
}
```

## 手写步骤

1. `low` 指向表头。
2. `high` 指向表尾。
3. 当 `low < high` 时交换两端元素。
4. `low` 后移，`high` 前移。
5. 两个下标相遇或交错时停止。

## 常见错误

- 循环条件写错，导致重复交换。
- 空表时没有注意 `high = length - 1` 的边界含义。
- 只移动一个下标，造成死循环。
- 用额外数组实现时忘记题目可能要求原地逆置。

## 典型题型

- 原地逆置顺序表。
- 判断奇数个元素时中间元素是否需要移动。
- 比较顺序表逆置和链表逆置的差异。

## 复杂度分析

时间复杂度：O(n)。

额外空间复杂度：O(1)。

交换次数约为 n / 2。

## 与其他知识的联系

顺序表逆置依赖下标随机访问。

它和双指针思想、数组原地交换、链表逆置有关。

## Obsidian 风格相关链接

- [[SeqList_Reverse]]
- [[SeqList_Insert_Delete]]
- [[LinkedList_Insert_Delete]]

## 待追问问题

- 链表逆置为什么不能直接用下标交换？
- 元素对象很大时，交换成本如何考虑？

## 来源

- knowledge_base/raw/data_structure/seq_list_reverse.txt
