# Stack Applications Basic

## 核心概念

栈遵循后进先出。

很多“最近出现的内容先处理”的问题适合用栈。

典型应用：

- 括号匹配
- 表达式求值
- 递归调用栈
- DFS

表达式求值通常会用操作数栈和运算符栈。

递归调用时，系统会用调用栈保存未完成的函数状态。

DFS 的回退过程与栈的后进先出特性有关。

## 考试识别信号

- 题目要求判断括号序列是否合法。
- 题目出现“最近未匹配的左括号”。
- 题目问递归为什么会占用栈空间。
- 题目问 DFS 与栈的关系。

## 核心公式 / 代码模板

括号匹配模板：

```cpp
bool Match(char left, char right) {
    return (left == '(' && right == ')') ||
           (left == '[' && right == ']') ||
           (left == '{' && right == '}');
}

bool BracketMatch(const char s[]) {
    const int MaxSize = 1000;
    char st[MaxSize];
    int top = -1;

    for (int i = 0; s[i] != '\0'; ++i) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            if (top == MaxSize - 1) return false;
            st[++top] = c;
        } else if (c == ')' || c == ']' || c == '}') {
            if (top == -1) return false;
            if (!Match(st[top], c)) return false;
            --top;
        }
    }

    return top == -1;
}
```

非括号字符直接跳过，不入栈也不出栈。

## 手写步骤 / 计算步骤

括号匹配：

1. 遇到左括号就入栈。
2. 入栈前检查栈满。
3. 遇到右括号先判断栈是否为空。
4. 如果栈空，匹配失败。
5. 如果栈非空，取栈顶左括号与当前右括号比较。
6. 匹配则出栈，不匹配则失败。
7. 扫描结束后，栈空才成功。

## 边界条件

空字符串：

没有括号需要匹配，通常认为匹配成功。

只有右括号：

遇到右括号时栈空，匹配失败。

只有左括号：

扫描结束后栈不空，匹配失败。

不同类型括号交叉：

如 `([)]`，数量相同但顺序不合法。

## 常见错误

- 入栈前没有检查栈满，可能数组越界。
- 遇到右括号时没有先判空。
- 扫描结束后忘记判断栈是否为空。
- 只判断括号数量相同，不判断类型和顺序。
- 出栈时 `top` 更新错误。

## 典型题型

- 判断括号序列是否合法。
- 写括号匹配算法。
- 说明递归调用栈。
- 说明 DFS 与栈的关系。

## 复杂度分析

括号匹配只扫描一次字符串。

时间复杂度：O(n)。

空间复杂度：O(n)，最坏情况下所有字符都是左括号。

## 与其他知识的联系

栈是受限线性表。

DFS 可以用递归隐式栈，也可以用显式栈。

## 相关链接

- [[Stack_Applications_Basic]]
- [[Stack_Queue_Basic]]
- [[Algorithm_Properties_Complexity]]

## 待追问问题

- 表达式求值中操作数栈和运算符栈如何配合？
- DFS 的递归写法和非递归写法如何互相转换？

## 来源

- knowledge_base/raw/data_structure/stack_applications_basic.txt
