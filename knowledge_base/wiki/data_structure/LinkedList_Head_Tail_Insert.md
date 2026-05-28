# LinkedList Head Tail Insert

## 核心概念

本页讨论带头结点单链表的头插法和尾插法。

头结点不存放有效数据，只用于统一空表和非空表的操作。

头插法把新结点插到头结点之后，常用于逆序建表。

尾插法把新结点插到当前尾结点之后，常用于保持输入顺序建表。

所有模板默认 `head` 是有效头结点指针，不是 `nullptr`。

考试手写模板默认 `new` 成功，一般不处理 `new` 失败。

## 核心代码模板

```cpp
struct LNode {
    int data;
    LNode* next;
};

void HeadInsert(LNode* head, int x) {
    LNode* s = new LNode{x, nullptr};
    s->next = head->next;
    head->next = s;
}

void TailInsert(LNode* head, int x) {
    LNode* tail = head;
    while (tail->next != nullptr) {
        tail = tail->next;
    }

    LNode* s = new LNode{x, nullptr};
    tail->next = s;
}
```

连续尾插建表时应维护 `tail`：

```cpp
void TailAppend(LNode*& tail, int x) {
    LNode* q = new LNode{x, nullptr};
    tail->next = q;
    tail = q;
}
```

## 手写步骤

头插法：

1. 创建新结点 `s`。
2. 令 `s->next = head->next`。
3. 令 `head->next = s`。

尾插法：

1. 找到当前尾结点 `tail`。
2. 创建新结点 `s`。
3. 令 `s->next = nullptr`。
4. 令 `tail->next = s`。

连续尾插建表：

1. 维护 `tail` 指针。
2. 每插入一个新结点 `q` 后，令 `tail->next = q`。
3. 再令 `tail = q`。
4. 保证 `q->next == nullptr`。

## 边界条件

空表：

`head->next == nullptr`，头插和尾插都可以直接执行。

尾插时，空表中的 `head` 本身就是尾结点。

只有一个有效结点：

插入时仍要保持原链表不断链。

## 常见错误

- 头插时先写 `head->next = s`，导致原首元结点丢失。
- 尾插时没有把新结点 `next` 置为 `nullptr`。
- 把头结点当作有效数据结点处理。
- 连续尾插建表时每次从头找尾，导致整体可能退化为 O(n^2)。
- 维护 `tail` 指针时，插入后忘记 `tail = q`。
- 常见错题反馈：[[LinkedList_Mistakes]]

## 识别信号

- 题目要求建立带头结点单链表。
- 题目出现头插法或尾插法。
- 题目要求保持输入顺序，通常想到尾插法。
- 题目要求逆序建立链表，通常想到头插法。

## 典型题型

- 用头插法建立带头结点单链表。
- 用尾插法建立带头结点单链表。
- 比较头插法和尾插法得到的结点顺序。
- 分析连续尾插建表是否需要维护尾指针。

## 复杂度分析

头插一次：O(1)。

单次尾插如果每次从 `head` 找尾：O(n)。

连续尾插建表如果维护 `tail`：整体 O(n)。

连续尾插建表如果每次从头找尾：整体可能 O(n^2)。

## 与其他知识的联系

头插法是单链表逆置的重要基础。

尾插法和有序链表合并中的尾指针维护类似。

链表插入的核心是先接后继，再改前驱。

## 相关链接

- [[LinkedList_Head_Tail_Insert]]
- [[LinkedList_Insert_Delete]]
- [[LinkedList_Reverse]]
- [[LinkedList_Ordered_Merge]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

## 待追问问题

- 连续尾插建表时，`tail` 应该由函数返回还是作为引用参数传入？
- 不带头结点链表的头插法需要额外处理哪些边界？

## 来源

- knowledge_base/raw/data_structure/linked_list_head_tail_insert.txt
