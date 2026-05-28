# LinkedList Mistakes

## 核心概念

本页记录链表手写题中的典型错误。

链表题的核心风险通常不是计算公式，而是指针顺序、断链、漏删和释放后访问。

## 插入时先写 p->next = q

错误现象：

在结点 `p` 后插入新结点 `q` 时，先执行 `p->next = q`。

后果：

原本 `p` 后面的结点会丢失入口，链表后半部分可能断开。

原因：

没有先让新结点接上原后继。

正确思路：

先执行 `q->next = p->next`。

再执行 `p->next = q`。

关联 wiki：

- [[LinkedList_Insert_Delete]]
- [[LinkedList_Head_Tail_Insert]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目要求在某结点后插入。
- 代码中先出现 `p->next = q`。
- 插入后原后继结点不再可达。

## 删除结点时没有先保存待删结点

错误现象：

删除结点时直接修改前驱指针，没有先保存待删结点。

后果：

可能无法释放待删结点，或者造成断链错误。

原因：

删除前没有保存 `q = p->next` 或当前待删结点指针。

正确思路：

先保存待删结点。

再断链。

最后释放待删结点。

关联 wiki：

- [[LinkedList_Insert_Delete]]
- [[LinkedList_Delete_Value]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目要求删除某结点或某结点后继。
- 代码中先改 `next`，但没有保存待删结点。
- 删除后无法 `delete` 正确结点。

## 删除值为 x 后 pre 也后移

错误现象：

删除链表中所有值为 `x` 的结点时，删除一个结点后 `pre` 也向后移动。

后果：

连续 `x` 会漏删。

原因：

删除当前结点后，下一个结点已经接到 `pre` 后面。

如果此时 `pre` 后移，就跳过了刚接上来的结点。

正确思路：

命中 `x` 时先保存 `next = p->next`。

断链并 `delete p`。

然后令 `p = next`。

删除后 `pre` 不动。

关联 wiki：

- [[LinkedList_Delete_Value]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目要求删除所有值为 `x` 的结点。
- 测试数据可能包含连续 `x`。
- 删除分支里同时移动了 `pre` 和 `p`。

## 链表逆置时忘记先保存 next

错误现象：

逆置链表时直接修改 `p->next`，没有先保存 `p` 的后继。

后果：

原链表后续部分可能断开，无法继续遍历。

原因：

当前结点的 `next` 被改写后，原来的后继入口丢失。

正确思路：

每次处理当前结点前，先保存 `next = p->next`。

再改变 `p->next`。

最后令 `p = next` 继续处理。

关联 wiki：

- [[LinkedList_Reverse]]
- [[LinkedList_Head_Tail_Insert]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目要求单链表逆置。
- 代码中修改 `p->next` 前没有保存 `next`。
- 逆置后只剩部分结点可达。

## 尾插法忘记 q->next = nullptr

错误现象：

尾插新结点后，没有把新结点的 `next` 置为空。

后果：

尾结点可能指向不确定位置，链表遍历可能出错。

原因：

尾结点的定义是 `next == nullptr`。

正确思路：

创建新结点时写 `LNode* q = new LNode{x, nullptr}`。

或者在接入前显式写 `q->next = nullptr`。

关联 wiki：

- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Insert_Delete]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目使用尾插法。
- 代码创建新结点后没有初始化 `next`。
- 遍历链表时无法正常停止。

## 连续尾插没有维护 tail 指针

错误现象：

连续尾插建表时，每插入一个结点都从头结点重新找尾。

后果：

整体时间复杂度可能退化为 O(n^2)。

原因：

每次找尾都是一次线性扫描。

正确思路：

建表时维护 `tail` 指针。

每次插入新结点 `q` 后，执行 `tail->next = q`，再执行 `tail = q`。

关联 wiki：

- [[LinkedList_Head_Tail_Insert]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目要求用尾插法建立链表。
- 插入过程在循环内反复从 `head` 找尾。
- 数据规模较大时操作次数明显增加。

## 有序链表合并后仍把 A/B 当原链表使用

错误现象：

合并两个有序单链表后，仍然把 `A` 和 `B` 当作原链表继续使用。

后果：

对链表结构的理解会出错，后续操作可能访问已经转移到结果链表中的数据结点。

原因：

合并模板复用 `A/B` 的数据结点。

这些数据结点已经被摘下并接入结果链表 `C`。

正确思路：

合并后应把 `C` 看作新的结果链表。

原 `A/B` 的数据结点已经转移。

如果保留 `A/B` 头结点，可以释放它们，或将它们的 `next` 置空。

关联 wiki：

- [[LinkedList_Ordered_Merge]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]

识别信号：

- 题目要求复用原结点合并。
- 合并模板中没有新建数据结点。
- 结果链表 `C` 接收了来自 `A/B` 的结点。

## 相关链接

- [[LinkedList_Insert_Delete]]
- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Reverse]]
- [[LinkedList_Delete_Value]]
- [[LinkedList_Ordered_Merge]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]

## 待追问问题

- 是否需要补充链表错题的图示版本？
- 是否需要整理双链表删除错题？

## 来源

- 链表专题练习错题反馈整理。
