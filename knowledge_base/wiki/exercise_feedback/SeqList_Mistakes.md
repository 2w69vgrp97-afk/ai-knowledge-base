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

## Obsidian 风格相关链接

- [[SeqList_Insert_Delete]]
- [[SeqList_Delete_All_X]]
- [[SeqList_Reverse]]
- [[DataStructure_Problem_Patterns]]
- [[DataStructure_Code_Templates]]

## 待追问问题

- 是否需要补充 1-based 下标版本的边界错误？
- 是否需要把链表、栈队列和二叉树错题也各建一页？

## 来源

- 顺序表练习错题反馈整理。
