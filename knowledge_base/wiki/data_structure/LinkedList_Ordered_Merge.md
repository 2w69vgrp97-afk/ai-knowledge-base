# LinkedList Ordered Merge

## 核心概念

本页讨论两个带头结点有序单链表的合并。

输入链表已经按同一方向有序。

合并时可以复用 `A/B` 的数据结点，把它们摘下后接到新结果链表 `C` 的尾部。

模板默认 `A` 和 `B` 是有效头结点指针，不是 `nullptr`。

考试手写模板默认 `new` 成功，一般不处理 `new` 失败。

## 核心代码模板

```cpp
struct LNode {
    int data;
    LNode* next;
};

LNode* MergeOrdered(LNode* A, LNode* B) {
    LNode* C = new LNode{0, nullptr};
    LNode* tail = C;
    LNode* p = A->next;
    LNode* q = B->next;

    while (p != nullptr && q != nullptr) {
        if (p->data <= q->data) {
            LNode* next = p->next;
            tail->next = p;
            tail = p;
            tail->next = nullptr;
            p = next;
        } else {
            LNode* next = q->next;
            tail->next = q;
            tail = q;
            tail->next = nullptr;
            q = next;
        }
    }

    tail->next = (p != nullptr) ? p : q;
    return C;
}
```

## 手写步骤

1. 创建结果链表头结点 `C`。
2. `tail` 指向结果链表尾结点。
3. `p` 扫描 `A` 的首元结点。
4. `q` 扫描 `B` 的首元结点。
5. 比较 `p` 和 `q` 的数据。
6. 摘下较小结点接到 `tail` 后面。
7. 令 `tail = 被接结点`。
8. 立即令 `tail->next = nullptr`，明确当前结点已从原链表摘下。
9. 某个链表为空后，接上另一个链表剩余部分。

## 边界条件

`A` 为空：

结果应接上 `B` 的有效结点。

`B` 为空：

结果应接上 `A` 的有效结点。

两个链表都为空：

结果为空链表。

存在相等元素：

如果希望稳定，可先接 `A` 中的结点。

合并后：

`A/B` 的数据结点已经转移到 `C`。

原 `A/B` 不应再按原链表使用。

如果保留 `A/B` 头结点，可以释放它们，或将它们的 `next` 置空。

## 常见错误

- 忘记保存 `next`，导致接入结果链表后丢失原链表后续部分。
- 忘记移动 `tail`，导致结果链表连接错误。
- 摘下结点后没有及时令 `tail->next = nullptr`，导致临时残链关系混乱。
- 忘记接上剩余链表。
- 输入链表不是同向有序却直接使用有序合并。
- 误把头结点也当作有效数据结点合并。
- 常见错题反馈：[[LinkedList_Mistakes]]

## 识别信号

- 题目给出两个有序单链表。
- 题目要求合并后仍然有序。
- 题目使用带头结点单链表。
- 题目可能要求不额外申请数据结点。

## 典型题型

- 合并两个递增有序单链表。
- 合并时复用原链表结点。
- 分析相等元素时的稳定性。
- 判断合并后原 `A/B` 是否还能按原链表使用。

## 复杂度分析

时间复杂度：O(m + n)。

额外空间复杂度：O(1)，不计新建结果头结点。

如果将结果头结点也计入，额外空间是 O(1)。

## 与其他知识的联系

链表有序合并和顺序表有序合并都利用输入已有序。

顺序表合并通常写入数组结果表。

链表合并通过修改 `next` 复用原结点。

## 相关链接

- [[LinkedList_Ordered_Merge]]
- [[LinkedList_Insert_Delete]]
- [[SeqList_Ordered_Merge]]
- [[SeqList_vs_LinkedList]]
- [[DataStructure_Code_Templates]]
- [[LinkedList_Mistakes]]

## 待追问问题

- 如果要求降序合并，比较条件如何改？
- 是否应该释放或复用原来的 `A/B` 头结点？

## 来源

- knowledge_base/raw/data_structure/linked_list_ordered_merge.txt
