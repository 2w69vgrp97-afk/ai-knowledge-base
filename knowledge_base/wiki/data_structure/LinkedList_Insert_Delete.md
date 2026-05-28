# LinkedList Insert Delete

## 核心概念

链表通过结点之间的指针表达逻辑顺序。

链表插入和删除的核心不是移动元素，而是修改结点之间的连接关系。

## 核心代码模板

```cpp
struct Node {
    int data;
    Node* next;
};

void insertAfter(Node* p, int value) {
    if (p == nullptr) return;

    Node* s = new Node{value, nullptr};
    s->next = p->next;
    p->next = s;
}

bool deleteAfter(Node* p) {
    if (p == nullptr) return false;

    Node* q = p->next;
    if (q == nullptr) return false;

    p->next = q->next;
    delete q;
    return true;
}
```

## 手写步骤

在结点 `p` 后插入新结点 `s`：

1. 创建新结点 `s`。
2. 令 `s->next = p->next`。
3. 令 `p->next = s`。

删除 `p` 后面的结点：

1. 令 `q = p->next`。
2. 判断 `q != NULL`。
3. 令 `p->next = q->next`。
4. `delete q`。

## 常见错误

- 插入时先写 `p->next = s`，导致原后继结点丢失。
- 删除前没有判断 `q != NULL`。
- 删除后忘记 `delete q`。
- 认为链表插入删除一定是 O(1)，忽略查找位置的成本。
- 单链表删除某结点时忘记需要前驱结点。

## 典型题型

- 单链表指定结点后插入。
- 删除单链表中某结点的后继结点。
- 说明头结点的作用。
- 比较顺序表和链表的插入删除。

## 复杂度分析

已知前驱结点时，插入和删除指针修改为 O(1)。

若需要从头查找位置，整体通常为 O(n)。

额外空间：插入一个结点需要 O(1) 新空间；删除不需要额外线性空间。

## 与其他知识的联系

链表和顺序表是线性表的两种典型存储方式。

链表也可以实现栈、队列等结构。

## Obsidian 风格相关链接

- [[LinkedList_Insert_Delete]]
- [[SeqList_Insert_Delete]]
- [[Stack_Queue_Basic]]

## 待追问问题

- 头插法和尾插法分别适合什么场景？
- 双链表如何简化删除操作？
- 循环链表的尾结点如何判断？

## 来源

- knowledge_base/raw/data_structure/linked_list_insert_delete.txt
