# DataStructure Code Templates

## 核心概念

本页收录数据结构考试中常用的 C/C++ 手写模板。

代码尽量短，重点服务于默写、边界判断和步骤记忆。

## 基础结构

```cpp
const int MaxSize = 1000;

struct SeqList {
    int data[MaxSize];
    int length;
};

struct LNode {
    int data;
    LNode* next;
};

SeqList L{{}, 0};
```

手写步骤：

先写结构体，再写安全初始化。

最容易错的位置：

`length` 表示有效元素个数，不是数组最大容量。

`length` 必须初始化为 0，否则插入、删除和遍历都会使用不确定的表长。

## 顺序表 Insert

```cpp
bool Insert(SeqList& L, int i, int x) {
    if (L.length == MaxSize) return false;
    if (i < 0 || i > L.length) return false;

    for (int j = L.length; j > i; --j) {
        L.data[j] = L.data[j - 1];
    }
    L.data[i] = x;
    ++L.length;
    return true;
}
```

手写步骤：

判满，判位置，从后往前移动，写入新元素，表长加一。

最容易错的位置：

移动方向必须从后往前，否则会覆盖数据。

识别信号：

题目出现“第 i 个位置插入”或“插入后仍保持原相对顺序”。

## 顺序表 Delete

```cpp
bool Delete(SeqList& L, int i, int& x) {
    if (L.length == 0) return false;
    if (i < 0 || i >= L.length) return false;

    x = L.data[i];
    for (int j = i; j < L.length - 1; ++j) {
        L.data[j] = L.data[j + 1];
    }
    --L.length;
    return true;
}
```

手写步骤：

判空，判位置，保存被删元素，从前往后覆盖，表长减一。

最容易错的位置：

删除合法范围是 `0 <= i < length`，不同于插入。

识别信号：

题目出现“删除第 i 个元素”，且循环体通常是 `data[j] = data[j + 1]`。

## DeleteAllX 覆盖法

```cpp
void DeleteAllX(SeqList& L, int x) {
    int k = 0;
    for (int i = 0; i < L.length; ++i) {
        if (L.data[i] != x) {
            L.data[k++] = L.data[i];
        }
    }
    L.length = k;
}
```

手写步骤：

`k` 指向下一个写入位置，只保留不等于 x 的元素，最后更新表长。

最容易错的位置：

忘记 `L.length = k`。

识别信号：

题目出现“删除所有 x”，尤其样例中有连续 x 时，优先使用覆盖法。

## 顺序表 Reverse

```cpp
void Reverse(SeqList& L) {
    int low = 0;
    int high = L.length - 1;
    while (low < high) {
        int t = L.data[low];
        L.data[low] = L.data[high];
        L.data[high] = t;
        ++low;
        --high;
    }
}
```

手写步骤：

左右指针从两端向中间走，每次交换一对元素。

最容易错的位置：

循环条件写 `low < high`。

## 有序顺序表 Merge

```cpp
bool Merge(const SeqList& A, const SeqList& B, SeqList& C) {
    if (A.length + B.length > MaxSize) return false;

    int i = 0, j = 0, k = 0;
    while (i < A.length && j < B.length) {
        if (A.data[i] <= B.data[j]) C.data[k++] = A.data[i++];
        else C.data[k++] = B.data[j++];
    }
    while (i < A.length) C.data[k++] = A.data[i++];
    while (j < B.length) C.data[k++] = B.data[j++];
    C.length = k;
    return true;
}
```

手写步骤：

双表同时扫描，较小者写入结果表，最后复制剩余元素。

最容易错的位置：

忘记复制某个表的剩余元素。

模板前提：

输出表 `C` 应是独立结果表，不应直接与输入表 `A` 或 `B` 混用。

否则可能边读边写，导致结果不可靠。

## 单链表 Insert

```cpp
void InsertAfter(LNode* p, int x) {
    if (p == nullptr) return;

    LNode* s = new LNode;
    s->data = x;
    s->next = p->next;
    p->next = s;
}
```

手写步骤：

创建新结点，先让新结点指向原后继，再让前驱指向新结点。

最容易错的位置：

不能先写 `p->next = s`。

## 单链表 Delete

```cpp
bool DeleteAfter(LNode* p) {
    if (p == nullptr) return false;

    LNode* q = p->next;
    if (q == nullptr) return false;

    p->next = q->next;
    delete q;
    return true;
}
```

手写步骤：

保存待删结点，判空，断链，释放结点。

最容易错的位置：

必须先保存 `q = p->next`，并判断 `q != nullptr`。

## 头插法

```cpp
void HeadInsert(LNode* head, int x) {
    LNode* s = new LNode{x, nullptr};
    s->next = head->next;
    head->next = s;
}
```

手写步骤：

创建新结点，先令 `s->next = head->next`，再令 `head->next = s`。

最容易错的位置：

不能先改 `head->next`，否则原首元结点会丢失。

调用前提：

默认带头结点单链表；`head` 是有效头结点指针，不是 `nullptr`；默认 `new` 成功。

常见错题反馈：[[LinkedList_Mistakes]]

## 尾插法

单次尾插：

```cpp
void TailInsert(LNode* head, int x) {
    LNode* tail = head;
    while (tail->next != nullptr) {
        tail = tail->next;
    }

    LNode* q = new LNode{x, nullptr};
    tail->next = q;
}
```

连续尾插建表：

```cpp
void TailAppend(LNode*& tail, int x) {
    LNode* q = new LNode{x, nullptr};
    tail->next = q;
    tail = q;
}
```

手写步骤：

新结点 `q->next = nullptr`，接到 `tail` 后面，再令 `tail = q`。

最容易错的位置：

连续尾插时忘记 `tail = q`，或忘记 `q->next = nullptr`。

调用前提：

默认带头结点单链表；`head` 或 `tail` 是有效指针；默认 `new` 成功。

常见错题反馈：[[LinkedList_Mistakes]]

## 单链表逆置

```cpp
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

手写步骤：

先保存 `next`，再把 `p` 头插到 `head` 后面，最后令 `p = next`。

最容易错的位置：

逆置时必须先保存 `next`，否则会断链。

调用前提：

默认带头结点单链表；`head` 是有效头结点指针，不是 `nullptr`。

常见错题反馈：[[LinkedList_Mistakes]]

## 删除所有值为 x 的结点

```cpp
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

手写步骤：

命中 `x` 时保存 `next`，断链，释放 `p`，再令 `p = next`。

最容易错的位置：

删除值为 `x` 时删除后 `pre` 不动，`p = next`，这样才能处理连续 `x`。

调用前提：

默认带头结点单链表；`head` 是有效头结点指针，不是 `nullptr`。

常见错题反馈：[[LinkedList_Mistakes]]

## 合并两个有序单链表

```cpp
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

手写步骤：

比较 `p/q`，摘下较小结点接到 `tail` 后面，移动 `tail`，再断开 `tail->next`。

最容易错的位置：

有序合并时复用原结点，接入 `tail` 后必须写 `tail->next = nullptr`。

合并后 `A/B` 的数据结点已转移，原 `A/B` 不应再按原链表使用。

调用前提：

默认带头结点单链表；`A/B` 是有效头结点指针，不是 `nullptr`；默认 `new` 成功。

常见错题反馈：[[LinkedList_Mistakes]]

## 顺序栈 Push / Pop

```cpp
struct SqStack {
    int data[MaxSize];
    int top;
};

SqStack S{{}, -1};

bool Push(SqStack& S, int x) {
    if (S.top == MaxSize - 1) return false;
    S.data[++S.top] = x;
    return true;
}

bool Pop(SqStack& S, int& x) {
    if (S.top == -1) return false;
    x = S.data[S.top--];
    return true;
}
```

手写步骤：

先初始化 `SqStack S{{}, -1};`。

约定 `top = -1` 表示空栈。入栈先加 `top` 再写，出栈先读再减 `top`。

最容易错的位置：

`top` 初值、判空、判满必须使用同一套约定。

## 循环队列 EnQueue / DeQueue

```cpp
struct SqQueue {
    int data[MaxSize];
    int front;
    int rear;
};

SqQueue Q{{}, 0, 0};

bool EnQueue(SqQueue& Q, int x) {
    if ((Q.rear + 1) % MaxSize == Q.front) return false;
    Q.data[Q.rear] = x;
    Q.rear = (Q.rear + 1) % MaxSize;
    return true;
}

bool DeQueue(SqQueue& Q, int& x) {
    if (Q.front == Q.rear) return false;
    x = Q.data[Q.front];
    Q.front = (Q.front + 1) % MaxSize;
    return true;
}
```

手写步骤：

先初始化 `SqQueue Q{{}, 0, 0};`。

队空是 `front == rear`。牺牲一个单元时，队满是 `(rear + 1) % MaxSize == front`。

最容易错的位置：

`front` 和 `rear` 必须初始化为 0。

每次移动 `front` 或 `rear` 都要取模。

## 二分查找

```cpp
int BinarySearch(int a[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
```

手写步骤：

取中间元素比较，目标较大则查右半，目标较小则查左半。

最容易错的位置：

更新区间时要排除 `mid`。

## 插入排序

```cpp
void InsertSort(int a[], int n) {
    for (int i = 1; i < n; ++i) {
        int x = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > x) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = x;
    }
}
```

手写步骤：

取当前元素，在前方有序区中移动比它大的元素，再插入空位。

最容易错的位置：

循环结束后插入位置是 `j + 1`。

## 冒泡排序

```cpp
void BubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; ++j) {
            if (a[j] > a[j + 1]) {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}
```

手写步骤：

相邻元素两两比较，大的向后交换，每趟确定一个最大元素。

最容易错的位置：

内层循环终点是 `n - 1 - i`。

## 选择排序

```cpp
void SelectSort(int a[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        int minPos = i;
        for (int j = i + 1; j < n; ++j) {
            if (a[j] < a[minPos]) minPos = j;
        }
        int t = a[i];
        a[i] = a[minPos];
        a[minPos] = t;
    }
}
```

手写步骤：

每趟从未排序区选出最小元素，放到未排序区最前面。

最容易错的位置：

选择排序通常不稳定。

## 快速排序 Partition

相关知识页：

- [[QuickSort_Partition]]

```cpp
int Partition(int a[], int low, int high) {
    int pivot = a[low];
    while (low < high) {
        while (low < high && a[high] >= pivot) --high;
        a[low] = a[high];
        while (low < high && a[low] <= pivot) ++low;
        a[high] = a[low];
    }
    a[low] = pivot;
    return low;
}
```

手写步骤：

保存枢轴，从右侧找小元素填左坑，从左侧找大元素填右坑，最后把枢轴放回最终位置。

最容易错的位置：

枢轴值必须先保存，循环中不能丢失。

调用前提：

`Partition` 只在 `low <= high` 且区间非空时调用。

通常由 `QuickSort` 的 `if (low < high)` 保证。

如果区间为空，`pivot = a[low]` 会有越界风险。

## Obsidian 风格相关链接

- [[DataStructure_Problem_Patterns]]
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
- [[Search_Basic]]
- [[Sort_Basic]]
- [[QuickSort_Partition]]

## 待追问问题

- 是否需要把这些模板改成教材使用的 1-based 下标版本？
- 是否需要单独整理二叉树递归遍历和层次遍历模板？

## 来源

- knowledge_base/wiki/data_structure/
