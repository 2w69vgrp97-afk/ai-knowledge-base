# Stack Queue Basic

## 核心概念

栈和队列都是受限线性表。

栈只允许在同一端插入和删除，体现后进先出。

队列通常在队尾插入、队头删除，体现先进先出。

## 核心代码模板

```cpp
struct CircularQueue {
    int data[1000];
    int front = 0;
    int rear = 0;
    int maxsize = 1000;
};

bool empty(const CircularQueue& q) {
    return q.front == q.rear;
}

bool full(const CircularQueue& q) {
    return (q.rear + 1) % q.maxsize == q.front;
}

bool enqueue(CircularQueue& q, int value) {
    if (full(q)) return false;
    q.data[q.rear] = value;
    q.rear = (q.rear + 1) % q.maxsize;
    return true;
}

bool dequeue(CircularQueue& q, int& value) {
    if (empty(q)) return false;
    value = q.data[q.front];
    q.front = (q.front + 1) % q.maxsize;
    return true;
}
```

## 手写步骤

栈：

1. 入栈时把元素放到栈顶。
2. 出栈时从栈顶取元素。
3. 判断栈空或栈满。

循环队列：

1. `front` 通常指向队头元素。
2. `rear` 通常指向下一个可插入位置。
3. 入队移动 `rear`。
4. 出队移动 `front`。
5. 下标移动使用取模。

## 常见错误

- 混淆栈的后进先出和队列的先进先出。
- 循环队列忘记取模。
- 用 `front == rear` 同时表示队空和队满，却没有额外区分条件。
- 牺牲一个单元时仍然认为可存放 `maxsize` 个元素。
- 使用 `count` 变量时忘记入队加一、出队减一。

## 典型题型

- 判断出栈序列是否合法。
- 用循环队列写入队和出队。
- 判断循环队列队空、队满。
- 解释队列假溢出。
- 说明递归和栈的关系。

## 复杂度分析

顺序栈入栈、出栈通常为 O(1)。

循环队列入队、出队通常为 O(1)。

顺序实现需要固定容量。

链式实现容量更灵活，但需要维护指针。

## 与其他知识的联系

栈和递归、括号匹配、表达式求值有关。

队列和层次遍历、任务调度有关。

循环队列可以看作顺序表空间复用的一种方式。

## Obsidian 风格相关链接

- [[Stack_Queue_Basic]]
- [[SeqList_Insert_Delete]]
- [[LinkedList_Insert_Delete]]
- [[BinaryTree_Basic]]

## 待追问问题

- 使用 `count` 判满和牺牲一个单元判满有什么取舍？
- 链队列为什么常设置队头和队尾指针？

## 来源

- knowledge_base/raw/data_structure/stack_queue_basic.txt
