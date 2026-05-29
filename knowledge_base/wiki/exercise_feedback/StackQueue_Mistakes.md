# StackQueue Mistakes

## 核心概念

本页记录栈和队列相关题目中的典型错误。

重点是把做题时容易忽略的边界条件沉淀成可复查的错误信号。

## 括号匹配遇到右括号时直接出栈

错误现象：

扫描表达式时，一遇到右括号就直接出栈匹配。

后果：

如果表达式以右括号开头，或右括号数量多于左括号，会在空栈上出栈，导致结果错误或访问无效栈顶。

原因：

只记住“右括号匹配栈顶左括号”，但忘记匹配前必须先确认栈非空。

正确思路：

遇到右括号时必须先判断栈是否为空。

若栈空，说明没有对应左括号，匹配失败。

若栈非空，再检查栈顶左括号类型是否匹配。

关联 wiki：

- [[Stack_Applications_Basic]]
- [[Stack_Queue_Basic]]
- [[DataStructure_Code_Templates]]

识别信号：

- 表达式可能以 `)`、`]`、`}` 开头。
- 右括号数量可能多于左括号。
- 代码中右括号分支直接读取或弹出栈顶。

## Obsidian 风格相关链接

- [[Stack_Applications_Basic]]
- [[Stack_Queue_Basic]]
- [[DataStructure_Code_Templates]]
- [[DataStructure_Problem_Patterns]]

## 待追问问题

- 是否需要补充循环队列队空、队满条件混淆的错题？
- 是否需要补充链队列最后一个结点出队后 `rear = front` 的错题？

## 来源

- 栈和队列选择题错题反馈整理。
