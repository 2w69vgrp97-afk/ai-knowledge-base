# Hash Chaining

## 核心概念

链地址法把散列到同一地址的关键字放入同一链表，这些关键字称为同义词。

哈希表每个位置保存链表头指针或头结点。插入时定位对应链表，查找时在链表中顺序比较。

## 考试识别信号

- 题目指定链地址法处理冲突。
- 画哈希表和各地址链表。
- 比较链地址法与线性探查。

## 核心公式 / 代码模板

```cpp
struct Node {
    int key;
    Node* next;
};

void Insert(Node* table[], int m, int key) {
    int idx = key % m;
    Node* p = new Node{key, table[idx]};
    table[idx] = p;
}
```

```cpp
Node* Search(Node* table[], int m, int key) {
    int idx = key % m;
    for (Node* p = table[idx]; p != nullptr; p = p->next) {
        if (p->key == key) return p;
    }
    return nullptr;
}
```

## 手写步骤 / 计算步骤

1. 计算散列地址。
2. 定位对应链表。
3. 插入时按题目要求头插或尾插。
4. 查找时沿链表逐个比较。

## 边界条件

空链表查找失败。链地址法需要额外指针空间，一般不会因为单个地址冲突而插入失败。

## 常见错误

- 忘记同义词放入同一链表。
- 把链地址法写成开放定址探查。
- 插入顺序与题目要求不一致。
- 画图时漏掉链表结点。

## 典型题型

- 用链地址法构造哈希表。
- 计算某关键字查找比较次数。
- 比较链地址法和线性探查的冲突处理。

## 复杂度分析

理想情况下链较短，查找接近 `O(1)`；若大量关键字落入同一链，最坏为 `O(n)`。

## 与其他知识的联系

链地址法属于 [[HashTable_Basic]]，与 [[LinkedList_Insert_Delete]] 中链表操作有关。

## 相关链接

- [[HashTable_Basic]]
- [[Hash_Linear_Probing]]
- [[LinkedList_Insert_Delete]]

## 待追问问题

- 链地址法 ASL 如何计算？
- 头插和尾插对查找序列有什么影响？

## 来源

- knowledge_base/raw/data_structure/hash_chaining.txt
