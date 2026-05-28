# LinkedList Delete Value

## 核心概念

本页讨论带头结点单链表中删除所有值等于 `x` 的结点。

删除结点时需要知道它的前驱结点。

带头结点可以让删除首元结点和删除中间结点使用同一套逻辑。

模板默认 `head` 是有效头结点指针，不是 `nullptr`。

考试手写模板默认 `new` 成功，一般不处理 `new` 失败。

## 核心代码模板

```cpp
struct LNode {
    int data;
    LNode* next;
};

void DeleteValue(LNode* head, int x) {
    LNode* pre = head;
    LNode* p = head->next;

    while (p != nullptr) {
        if (p->data == x) {
            LNode* next = p->next;
            pre->next = next;
            delete p;
            p = next;
        } else {
            pre = p;
            p = p->next;
        }
    }
}
```

## 手写步骤

1. `pre` 指向当前结点的前驱。
2. `p` 指向当前检查结点。
3. 如果 `p->data == x`，先保存 `next = p->next`。
4. 令 `pre->next = next`，把 `p` 从链表断开。
5. `delete p`。
6. 令 `p = next`，继续检查。
7. 如果 `p->data != x`，`pre` 和 `p` 同时后移。

## 边界条件

空表：

`head->next == nullptr`，循环不执行。

首元结点等于 `x`：

`pre` 是 `head`，可以统一删除。

连续多个 `x`：

删除后 `pre` 不动，`p` 后移到 `next`，可以连续删除。

没有 `x`：

只遍历，不删除。

全是 `x`：

最终 `head->next == nullptr`。

## 常见错误

- 删除时没有保存后继，导致断链。
- 删除后 `pre` 也后移，连续 `x` 会漏删。
- 释放 `p` 后再访问 `p->next`。
- 不使用头结点时，首元结点删除逻辑单独处理失败。
- 常见错题反馈：[[LinkedList_Mistakes]]

## 识别信号

- 题目要求删除链表中所有值为 `x` 的结点。
- 题目可能出现连续目标值。
- 题目使用带头结点单链表。
- 代码中需要同时维护 `pre` 和 `p`。

## 典型题型

- 删除带头结点单链表中所有值为 `x` 的结点。
- 处理连续目标值。
- 分析删除首元结点时头结点的作用。
- 找出 delete 后访问的风险。

## 复杂度分析

时间复杂度：O(n)。

额外空间复杂度：O(1)。

每个结点最多访问一次。

## 与其他知识的联系

链表删除靠断链和释放。

顺序表删除所有 `x` 通常靠移动或覆盖。

二者的核心差异是：顺序表处理数组位置，链表处理指针连接。

## 相关链接

- [[LinkedList_Delete_Value]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_Delete_All_X]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

## 待追问问题

- 如果只删除第一个值为 `x` 的结点，循环如何提前结束？
- 不带头结点时删除首元结点如何处理？

## 来源

- knowledge_base/raw/data_structure/linked_list_delete_value.txt
