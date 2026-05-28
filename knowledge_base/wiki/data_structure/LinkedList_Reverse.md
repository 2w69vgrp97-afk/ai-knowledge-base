# LinkedList Reverse

## 核心概念

本页讨论带头结点单链表的原地逆置。

链表不能像顺序表那样通过下标直接交换两端元素。

单链表逆置的核心是逐个取下原链表中的结点，并用头插法插入到新链表头部。

模板默认 `head` 是有效头结点指针，不是 `nullptr`。

考试手写模板默认 `new` 成功，一般不处理 `new` 失败。

## 核心代码模板

```cpp
struct LNode {
    int data;
    LNode* next;
};

void ReverseList(LNode* head) {
    LNode* p = head->next;
    head->next = nullptr;

    while (p != nullptr) {
        LNode* next = p->next;
        p->next = head->next;
        head->next = p;
        p = next;
    }
}
```

## 手写步骤

1. 令 `p` 指向首元结点。
2. 将 `head->next` 置空，形成空的新链表。
3. 当 `p != nullptr` 时，先保存 `next = p->next`。
4. 将 `p` 用头插法插入到 `head` 后面。
5. 令 `p = next`，继续处理原链表后续结点。

## 边界条件

空表：

`head->next == nullptr`，循环不执行。

只有一个有效结点：

保存 `next` 后头插回去，结果仍然正确。

多个结点：

每次处理一个结点，必须保留未处理部分入口。

## 常见错误

- 没有先保存 `next`，导致链表断开后找不到后续结点。
- 忘记先令 `head->next = nullptr`，造成旧链和新链混在一起。
- 把顺序表交换两端元素的思路直接套到链表。
- 循环结束后没有令 `p = next`，导致死循环。
- 常见错题反馈：[[LinkedList_Mistakes]]

## 识别信号

- 题目要求单链表逆置。
- 题目要求不申请额外数组。
- 题目强调改变指针方向。
- 代码中需要保存当前结点的后继。

## 典型题型

- 原地逆置带头结点单链表。
- 比较顺序表逆置和单链表逆置。
- 找出链表逆置代码中的断链错误。

## 复杂度分析

时间复杂度：O(n)。

额外空间复杂度：O(1)。

每个有效结点只被摘下并头插一次。

## 与其他知识的联系

单链表逆置依赖头插法。

它体现了链表操作中“保存后继，防止断链”的核心原则。

## 相关链接

- [[LinkedList_Reverse]]
- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_Reverse]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

## 待追问问题

- 三指针逆置法和头插法逆置有什么区别？
- 不带头结点单链表逆置的边界如何处理？

## 来源

- knowledge_base/raw/data_structure/linked_list_reverse.txt
