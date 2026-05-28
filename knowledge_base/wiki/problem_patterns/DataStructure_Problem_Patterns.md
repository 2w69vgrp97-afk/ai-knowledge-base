# DataStructure Problem Patterns

## 核心概念

本页按考试题型整理数据结构常见手写题，不按章节顺序照搬。

使用时先识别题目要求，再跳转到对应知识页和代码模板。

## 顺序表插入删除

题型识别：

题目要求在顺序表第 i 个位置插入元素，或删除第 i 个元素。

对应知识页链接：

- [[SeqList_Insert_Delete]]
- [[DataStructure_Code_Templates]]
- [[SeqList_Mistakes]]

核心套路：

先判断空表、满表和位置合法性。

插入从后往前移动元素。

删除从前往后覆盖元素。

常见错误：

- 插入时移动方向写反。
- 插入和删除的位置合法范围混淆。
- 忘记更新 `length`。

## 删除顺序表中所有 x

题型识别：

题目要求删除顺序表中所有值等于 x 的元素，通常要求原地完成。

对应知识页链接：

- [[SeqList_Delete_All_X]]
- [[SeqList_Insert_Delete]]
- [[DataStructure_Code_Templates]]
- [[SeqList_Mistakes]]

核心套路：

使用覆盖法。

`k` 表示下一个非 x 元素的写入位置。

扫描结束后必须令 `length = k`。

常见错误：

- 每遇到一个 x 就整体删除，导致重复移动。
- 忘记处理全是 x 或没有 x。
- 忘记更新表长。

## 顺序表逆置

题型识别：

题目要求把顺序表中的元素原地逆序。

对应知识页链接：

- [[SeqList_Reverse]]
- [[DataStructure_Code_Templates]]

核心套路：

使用左右双指针。

`low` 从表头开始，`high` 从表尾开始。

当 `low < high` 时交换元素。

常见错误：

- 循环条件写成 `low <= high` 导致多余操作。
- 只移动一个指针。
- 忘记空表和单元素表不需要交换。

## 合并两个有序顺序表

题型识别：

题目给出两个递增或递减顺序表，要求合并成一个仍有序的顺序表。

对应知识页链接：

- [[SeqList_Ordered_Merge]]
- [[Sort_Basic]]
- [[DataStructure_Code_Templates]]

核心套路：

用 `i`、`j` 分别扫描两个输入表。

用 `k` 写入结果表。

每次取当前较小元素，最后复制剩余元素。

常见错误：

- 忘记复制剩余部分。
- 忽略结果表容量。
- 两个输入表并非同向有序时仍直接套模板。

## 单链表插入删除

题型识别：

题目要求在某结点后插入，或删除某结点的后继结点。

对应知识页链接：

- [[LinkedList_Insert_Delete]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

核心套路：

插入时先让新结点接上原后继，再让前驱指向新结点。

删除时先保存 `q = p->next`，判断 `q != NULL`，再断链并释放。

常见错误：

- 插入时先改 `p->next`，丢失原后继。
- 删除前没有判空。
- 删除后没有释放结点。

## 头插法建表

题型识别：

题目要求用头插法建立带头结点单链表，或要求逆序建立链表。

对应知识页链接：

- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

核心套路：

创建新结点 `s`。

先令 `s->next = head->next`。

再令 `head->next = s`。

常见错误：

- 先改 `head->next`，导致原首元结点丢失。
- 把头结点当作有效数据结点。
- 忘记头插法会使输入顺序反过来。

## 尾插法建表

题型识别：

题目要求保持输入顺序建立带头结点单链表。

对应知识页链接：

- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

核心套路：

维护尾指针 `tail`。

新结点 `q->next = nullptr`。

令 `tail->next = q`，再令 `tail = q`。

常见错误：

- 忘记 `q->next = nullptr`。
- 连续尾插时每次从头找尾，整体可能退化为 O(n^2)。
- 插入后忘记 `tail = q`。

## 单链表逆置

题型识别：

题目要求原地逆置带头结点单链表。

对应知识页链接：

- [[LinkedList_Reverse]]
- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

核心套路：

逐个取下原链表结点。

先保存 `next = p->next`。

再用头插法把 `p` 插回 `head` 后面。

常见错误：

- 没有先保存 `next`，导致断链。
- 忘记先令 `head->next = nullptr`。
- 把顺序表两端交换的思路套到链表。

## 删除链表中所有值为 x 的结点

题型识别：

题目要求删除带头结点单链表中所有值为 `x` 的结点。

对应知识页链接：

- [[LinkedList_Delete_Value]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

核心套路：

`pre` 指向前驱，`p` 指向当前结点。

命中目标时先保存 `next = p->next`。

断链后 `delete p`，再令 `p = next`，删除后 `pre` 不动。

常见错误：

- 删除后 `pre` 也后移，连续 `x` 会漏删。
- 释放 `p` 后再访问 `p->next`。
- 忘记带头结点可以统一处理首元结点。

## 合并两个有序单链表

题型识别：

题目给出两个有序带头结点单链表，要求合并后仍然有序。

对应知识页链接：

- [[LinkedList_Ordered_Merge]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

核心套路：

使用 `C` 作为新结果头结点。

复用 `A/B` 的数据结点。

每次摘下较小结点接到 `tail` 后，令 `tail = 被接结点`，再令 `tail->next = nullptr`。

最后接上剩余链表。

常见错误：

- 忘记保存 `next`，导致丢失原链表后续部分。
- 忘记移动 `tail`。
- 忘记接上剩余链表。
- 合并后仍按原链表使用 `A/B`。

## 栈基本操作

题型识别：

题目要求入栈、出栈、判断栈空或栈满，或判断出栈序列。

对应知识页链接：

- [[Stack_Queue_Basic]]
- [[DataStructure_Code_Templates]]

核心套路：

顺序栈用 `top` 表示栈顶位置。

入栈先判满，再写入并更新 `top`。

出栈先判空，再取出并更新 `top`。

常见错误：

- `top` 初值和判空条件不一致。
- 先移动 `top` 还是先写数据的约定混乱。
- 忘记栈是后进先出。

## 循环队列

题型识别：

题目要求用数组实现队列，且需要解决假溢出。

对应知识页链接：

- [[Stack_Queue_Basic]]
- [[DataStructure_Code_Templates]]

核心套路：

`front` 指向队头元素。

`rear` 指向下一个可插入位置。

入队移动 `rear`，出队移动 `front`，移动时取模。

常见错误：

- 忘记取模。
- 队空和队满条件冲突。
- 牺牲一个单元时仍认为容量是 `maxsize`。

## 二叉树遍历

题型识别：

题目要求写前序、中序、后序或层次遍历，或根据遍历序列还原二叉树。

对应知识页链接：

- [[BinaryTree_Basic]]
- [[Stack_Queue_Basic]]

核心套路：

前序：根、左、右。

中序：左、根、右。

后序：左、右、根。

层次遍历使用队列。

还原二叉树时，用前序或后序确定根，用中序划分左右子树。

常见错误：

- 只有前序和后序就尝试唯一还原普通二叉树。
- 层次遍历不用队列。
- 完全二叉树编号从 0 开始和从 1 开始混用。

## 折半查找

题型识别：

题目给出有序顺序表，要求查找某关键字或写出比较过程。

对应知识页链接：

- [[Search_Basic]]
- [[SeqList_Insert_Delete]]
- [[DataStructure_Code_Templates]]

核心套路：

维护 `[low, high]` 区间。

取 `mid` 比较。

根据大小关系缩小一半区间。

`low > high` 时查找失败。

常见错误：

- 对无序表使用折半查找。
- 对普通单链表直接套用折半查找。
- 更新边界时没有排除 `mid`。

## 基础排序

题型识别：

题目要求写排序过程、判断稳定性、分析复杂度，或给出某一趟后的序列。

对应知识页链接：

- [[Sort_Basic]]
- [[Search_Basic]]
- [[SeqList_Ordered_Merge]]
- [[QuickSort_Partition]]
- [[DataStructure_Code_Templates]]

核心套路：

插入排序：把当前元素插入前方有序区。

冒泡排序：相邻比较交换。

选择排序：每趟选择最小或最大元素。

快速排序：先 partition，再递归处理左右区间。

常见错误：

- 只记时间复杂度，忘记稳定性。
- 把选择排序误认为稳定。
- 快排 partition 边界写错。
- 误以为一趟 partition 后整个序列已经有序。

## Obsidian 风格相关链接

- [[SeqList_Insert_Delete]]
- [[SeqList_Delete_All_X]]
- [[SeqList_Reverse]]
- [[SeqList_Ordered_Merge]]
- [[LinkedList_Insert_Delete]]
- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Reverse]]
- [[LinkedList_Delete_Value]]
- [[LinkedList_Ordered_Merge]]
- [[LinkedList_Mistakes]]
- [[Stack_Queue_Basic]]
- [[BinaryTree_Basic]]
- [[Search_Basic]]
- [[Sort_Basic]]
- [[QuickSort_Partition]]
- [[DataStructure_Code_Templates]]

## 待追问问题

- 哪些题型最适合整理成一页“默写清单”？
- 是否需要为每类题型补一组真题样例？

## 来源

- knowledge_base/wiki/data_structure/
