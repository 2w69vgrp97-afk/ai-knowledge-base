# Hash Linear Probing

## 核心概念

线性探查是开放定址法的一种。发生冲突后，依次检查下一个位置。

常见探查序列：

`H_i = (H(key) + i) % m, i = 0, 1, 2, ...`

取模用于到表尾后回到表头。

## 考试识别信号

- 题目指定线性探查处理冲突。
- 构造哈希表。
- 计算查找成功或失败的比较次数。

## 核心公式 / 代码模板

`EMPTY` 表示空位置，`DELETED` 表示删除标记。

```cpp
bool Insert(int h[], int m, int key) {
    int pos = key % m;
    for (int i = 0; i < m; ++i) {
        int j = (pos + i) % m;
        if (h[j] == EMPTY || h[j] == DELETED) {
            h[j] = key;
            return true;
        }
    }
    return false;
}
```

```cpp
int Search(int h[], int m, int key) {
    int pos = key % m;
    for (int i = 0; i < m; ++i) {
        int j = (pos + i) % m;
        if (h[j] == EMPTY) return -1;
        if (h[j] == key) return j;
    }
    return -1;
}
```

## 手写步骤 / 计算步骤

1. 计算初始地址。
2. 若冲突，依次检查下一个位置。
3. 到表尾后取模回到表头。
4. 最多探查 `m` 次。

## 边界条件

表满时插入失败。查找遇 `EMPTY` 可判失败，但遇 `DELETED` 不能立即失败。

## 常见错误

- 忘记取模回绕。
- 查找和插入探查序列不一致。
- 删除后直接置空，破坏查找链。
- 遇删除标记直接查找失败。

## 典型题型

- 手工构造线性探查哈希表。
- 求查找成功/失败比较次数。
- 判断删除标记处理是否正确。

## 复杂度分析

理想情况下接近 `O(1)`；冲突严重或装填因子过高时性能下降。线性探查容易产生堆积。

## 与其他知识的联系

线性探查属于 [[HashTable_Basic]] 的开放定址法。另一类方法是 [[Hash_Chaining]]。

## 相关链接

- [[HashTable_Basic]]
- [[Hash_Chaining]]
- [[Search_Basic]]

## 待追问问题

- 线性探查的 ASL 如何手算？
- 删除标记对查找失败长度有什么影响？

## 来源

- knowledge_base/raw/data_structure/hash_linear_probing.txt
