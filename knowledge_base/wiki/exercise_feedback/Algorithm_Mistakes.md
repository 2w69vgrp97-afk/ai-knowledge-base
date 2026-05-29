# Algorithm Mistakes

## 核心概念

本页记录算法性质和复杂度判断中的典型错误。

重点是识别循环规模如何变化，而不是只数循环嵌套层数。

## i *= 2 的循环误判为 O(n^2)

错误现象：

看到循环变量变化就误判为 `O(n^2)`，没有区分线性增长和倍增。

原因：

只凭循环外形判断复杂度，忽略了 `i *= 2` 每次都会让规模成倍增长。

正确思路：

`i *= 2` 的循环次数约为 `log2 n`。

因此：

```cpp
for (int i = 1; i < n; i *= 2) {
    // O(1)
}
```

时间复杂度是 `O(log n)`。

关联 wiki：

- [[Algorithm_Properties_Complexity]]
- [[Search_Basic]]
- [[DataStructure_Code_Templates]]

识别信号：

- `i *= 2`
- `i /= 2`
- 折半
- 二分

## Obsidian 风格相关链接

- [[Algorithm_Properties_Complexity]]
- [[Search_Basic]]
- [[DataStructure_Problem_Patterns]]

## 待追问问题

- 是否需要补充嵌套循环 `j < i` 的求和型复杂度错题？
- 是否需要补充最好、平均、最坏复杂度混淆的错题？

## 来源

- 算法复杂度选择题错题反馈整理。
