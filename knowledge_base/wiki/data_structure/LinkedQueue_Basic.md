# LinkedQueue Basic

## 核心概念

链队列是用链式存储实现的队列。

队列遵循先进先出。

带头结点链队列通常设置两个指针：

- `front` 指向头结点。
- `rear` 指向队尾结点。

空队时 `front == rear`。

## 考试识别信号

- 题目要求用链表实现队列。
- 题目出现 `front` 和 `rear` 指针。
- 题目要求入队、出队模板。
- 题目强调出队最后一个结点时 `rear` 如何处理。

## 核心公式 / 代码模板

```cpp
struct QNode {
    int data;
    QNode *next;
};

struct LinkQueue {
    QNode *front;
    QNode *rear;
};

void InitQueue(LinkQueue &Q) {
    Q.front = Q.rear = new QNode{0, nullptr};
}

bool IsEmpty(LinkQueue& Q) {
    return Q.front == Q.rear;
}

void EnQueue(LinkQueue& Q, int x) {
    QNode* s = new QNode{x, nullptr};
    Q.rear->next = s;
    Q.rear = s;
}

bool DeQueue(LinkQueue& Q, int& x) {
    if (Q.front == Q.rear) return false;

    QNode* p = Q.front->next;
    x = p->data;
    Q.front->next = p->next;

    if (Q.rear == p) {
        Q.rear = Q.front;
    }

    delete p;
    return true;
}
```

模板默认 `new` 成功，考试模板一般不处理 `new` 失败。

`front` 和 `rear` 必须先初始化为同一个有效头结点。

若未初始化就访问 `Q.rear->next`，会有空指针风险。

## 手写步骤 / 计算步骤

入队：

1. 创建新结点 `s`。
2. 令 `s->next = nullptr`。
3. 令 `rear->next = s`。
4. 令 `rear = s`。

出队：

1. 判断队空。
2. 保存首元结点 `p = front->next`。
3. 取出 `p->data`。
4. 令 `front->next = p->next`。
5. 如果 `p` 是最后一个结点，令 `rear = front`。
6. `delete p`。

## 边界条件

空队：

`front == rear`。

只有一个元素：

出队后必须令 `rear = front`。

出队最后一个结点后，`rear` 必须回到 `front`。

## 常见错误

- 没有调用 `InitQueue` 就访问 `Q.rear->next`。
- 出队前没有判空。
- 出队最后一个结点后没有让 `rear` 回到 `front`。
- 入队后忘记 `rear = s`。
- 删除结点后再访问该结点。

## 典型题型

- 写链队列初始化。
- 写链队列入队、出队。
- 判断空队条件。
- 说明最后一个结点出队时为什么要更新 `rear`。

## 复杂度分析

入队：O(1)。

出队：O(1)。

链队列不需要像循环队列那样移动数组下标。

## 与其他知识的联系

链队列是队列的链式实现。

循环队列是队列的顺序实现。

## 相关链接

- [[LinkedQueue_Basic]]
- [[Stack_Queue_Basic]]
- [[LinkedList_Insert_Delete]]
- [[DataStructure_Code_Templates]]

## 待追问问题

- 不带头结点链队列如何判断空队？
- 链队列如何销毁并释放所有结点？

## 来源

- knowledge_base/raw/data_structure/linked_queue_basic.txt
