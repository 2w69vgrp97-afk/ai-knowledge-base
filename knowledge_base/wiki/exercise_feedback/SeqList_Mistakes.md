# SeqList Mistakes

## 核心概念

本页记录顺序表手写题中的典型错误。

重点不是重新讲知识点，而是帮助做题时识别错误信号，快速回到正确套路。

## DeleteAllX 删除后 i++ 导致跳元素

错误现象：

在删除顺序表中所有 x 时，发现删除不干净。

例如连续出现两个 x，只删除了第一个，第二个被跳过。

原因：

如果采用“发现 x 就删除当前位置”的写法，删除后后面的元素会整体前移。

此时当前位置已经变成新的元素。

如果循环又执行 `i++`，就会跳过这个新移动到当前位置的元素。

正确思路：

优先使用覆盖法。

用 `k` 表示下一个非 x 元素的写入位置。

扫描原表时只保留 `data[i] != x` 的元素，最后令 `length = k`。

关联 wiki：

- [[SeqList_Delete_All_X]]
- [[SeqList_Insert_Delete]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目要求删除“所有 x”。
- 测试数据里有连续 x。
- 代码里出现删除后仍然无条件 `i++`。

## 插入时移动方向写反

错误现象：

顺序表插入后，部分原有元素丢失或被重复覆盖。

插入位置之后的数据不再正确。

原因：

顺序表插入需要给新元素腾出空位。

如果从插入位置向后移动，会先覆盖后一个元素，导致原数据丢失。

正确思路：

插入时必须从表尾向插入位置反向移动。

先移动 `data[length] = data[length - 1]`，再逐步向前。

最后把新元素写入插入位置，并令 `length++`。

关联 wiki：

- [[SeqList_Insert_Delete]]
- [[DataStructure_Code_Templates]]
- [[DataStructure_Problem_Patterns]]

识别信号：

- 题目关键词是“插入”。
- 代码中出现从小下标到大下标搬移元素。
- 插入后原顺序表后半部分异常。

## 删除循环边界写成 k < length

错误现象：

顺序表删除指定位置元素后，循环访问到了无效位置。

最后一次移动可能读取 `data[length]`。

原因：

删除第 i 个元素时，需要把后面的元素前移。

最后一次有效移动是把 `data[length - 1]` 移到 `data[length - 2]`。

如果循环写成 `k < length`，就可能访问越界或把无效尾部数据搬进表内。

正确思路：

删除循环应控制到 `k < length - 1`。

常见写法是：

```cpp
for (int k = i; k < L.length - 1; ++k) {
    L.data[k] = L.data[k + 1];
}
--L.length;
```

关联 wiki：

- [[SeqList_Insert_Delete]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目关键词是“删除第 i 个元素”。
- 循环体中有 `data[k] = data[k + 1]`。
- 循环边界写到了 `k < length`。

## 顺序表主要优点误认为“存储空间一定不浪费”

错误现象：

选择题把顺序表的主要优点选成“存储空间一定不浪费”。

原因：

混淆了顺序表的空间分配特点。

顺序表通常需要一段连续存储空间，静态顺序表还可能预留未使用容量，因此不能说存储空间一定不浪费。

正确思路：

顺序表的主要优点是随机访问快，支持按下标 `O(1)` 访问。

关联 wiki：

- [[SeqList_Insert_Delete]]
- [[LinearList_Basic]]
- [[Array_Basic]]

识别信号：

- 题目问“顺序表主要优点”。
- 选项中同时出现“随机访问”和“节省空间”。
- 题目强调按下标查找或第 i 个元素。

## 删除顺序表下标 i 的元素时，移动次数误写为 n-i

错误现象：

计算删除顺序表下标 `i` 的元素时，把移动次数写成 `n - i`。

原因：

把被删除元素本身也算进了移动次数。

正确思路：

真正移动的是 `a[i + 1]` 到 `a[n - 1]` 这些后续元素。

元素个数为 `n - i - 1`，因此删除下标 `i` 的元素需要移动 `n - i - 1` 次。

关联 wiki：

- [[SeqList_Insert_Delete]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目问“删除第 i 个元素后需要移动多少次”。
- 下标采用 0-based，顺序表长度为 `n`。
- 容易把 `a[i]` 也算入移动范围。

## Obsidian 风格相关链接

- [[SeqList_Insert_Delete]]
- [[SeqList_Delete_All_X]]
- [[SeqList_Reverse]]
- [[LinearList_Basic]]
- [[Array_Basic]]
- [[DataStructure_Problem_Patterns]]
- [[DataStructure_Code_Templates]]

## 待追问问题

- 是否需要补充 1-based 下标版本的边界错误？
- 是否需要把链表、栈队列和二叉树错题也各建一页？

## 来源

- 顺序表练习错题反馈整理。
