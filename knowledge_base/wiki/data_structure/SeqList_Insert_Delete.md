# SeqList Insert Delete

## 核心概念

顺序表用一段连续存储空间保存线性表元素。

它支持按下标快速访问，时间复杂度为 O(1)。

顺序表可能预分配连续空间，因此不能说“存储空间一定不浪费”。

插入和删除中间元素时，需要移动后续元素来保持逻辑顺序和物理顺序一致。

## 核心代码模板

```cpp
struct SeqList {
    int data[1000];
    int length = 0;
    int capacity = 1000;
};

bool insert(SeqList& list, int pos, int value) {
    if (list.length == list.capacity) return false;
    if (pos < 0 || pos > list.length) return false;

    for (int j = list.length; j > pos; --j) {
        list.data[j] = list.data[j - 1];
    }
    list.data[pos] = value;
    ++list.length;
    return true;
}

bool erase(SeqList& list, int pos) {
    if (list.length == 0) return false;
    if (pos < 0 || pos >= list.length) return false;

    for (int j = pos; j < list.length - 1; ++j) {
        list.data[j] = list.data[j + 1];
    }
    --list.length;
    return true;
}
```

## 手写步骤

插入：

1. 判断顺序表是否已满。
2. 判断插入位置是否合法。
3. 从表尾向插入位置反向移动元素。
4. 写入新元素。
5. 表长加 1。

删除：

1. 判断顺序表是否为空。
2. 判断删除位置是否合法。
3. 从删除位置后一位开始向前移动元素。
4. 表长减 1。

## 边界条件

空表：

不能删除元素。

满表：

不能继续普通插入，除非先扩容。

插入位置：

0-based 写法通常允许 `0 <= pos <= length`。

删除位置：

0-based 写法通常要求 `0 <= pos < length`。

表头操作：

插入或删除时移动元素最多。

表尾操作：

插入或删除时移动元素最少。

## 常见错误

- 插入时从前往后移动，导致元素被覆盖。
- 插入移动方向写反，会覆盖尚未移动的数据。
- 删除空表中的元素。
- 把插入合法范围和删除合法范围混淆。
- 表满时仍然插入。
- 忘记更新 `length`。
- 删除循环写成 `j < length`，导致访问 `data[length]`。
- 把顺序表主要优点误认为“存储空间一定不浪费”，忽略了随机访问才是核心优势。
- 删除下标 `i` 的元素时，把移动次数误写成 `n - i`。

## 典型题型

- 写出顺序表第 i 个位置插入元素的算法。
- 写出删除第 i 个元素的算法。
- 分析插入或删除时元素移动次数。
- 判断空表、满表、表头、表尾操作的边界。

## 识别信号

- 题目出现“在第 i 个位置插入”。
- 题目出现“删除第 i 个元素”。
- 插入题出现“腾出位置”或“元素后移”。
- 删除题出现“后续元素补位”或“元素前移”。
- 代码中需要把一段元素整体后移或前移。
- 插入题中如果循环从小下标到大下标移动，要警惕覆盖。
- 删除题中如果循环体是 `data[j] = data[j + 1]`，边界应特别检查。

## 复杂度分析

按下标访问：O(1)。

插入：通常 O(n)。

删除：通常 O(n)。

插入长度为 `n` 的顺序表中下标 `i` 的元素，需要移动 `n - i` 个元素。

删除长度为 `n` 的顺序表中下标 `i` 的元素，需要移动 `n - i - 1` 个元素。

若插入位置等概率出现，平均移动约 n / 2 个元素。

若删除位置等概率出现，平均移动约 (n - 1) / 2 个元素。

## 与其他知识的联系

顺序表适合随机访问。

链表适合在已知结点位置附近进行插入删除。

顺序表的移动元素思想会出现在删除所有 x、逆置、排序等题型中。

## Obsidian 风格相关链接

- [[SeqList_Insert_Delete]]
- [[SeqList_Delete_All_X]]
- [[SeqList_Reverse]]
- [[SeqList_Ordered_Merge]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_Mistakes]]
- [[SeqList_vs_LinkedList]]

## 待追问问题

- 不同教材中第 i 个位置是从 0 开始还是从 1 开始？
- 动态数组扩容时，插入复杂度如何分析？

## 来源

- knowledge_base/raw/data_structure/seq_list_insert_delete.txt
