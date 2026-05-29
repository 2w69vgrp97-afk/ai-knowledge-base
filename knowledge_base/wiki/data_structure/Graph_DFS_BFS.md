# Graph DFS BFS

## 核心概念

DFS 深度优先搜索沿一条路径尽可能深入，不能继续时回退。DFS 可用递归或栈实现。

BFS 广度优先搜索先访问起点的邻接点，再逐层向外扩展。BFS 使用队列。

访问序列受邻接点存储顺序影响。

## 考试识别信号

- 要求给出 DFS 或 BFS 访问序列。
- 判断图是否连通。
- 写图遍历伪代码。

## 核心公式 / 代码模板

DFS：

```cpp
void DFS(int v) {
    visited[v] = true;
    visit(v);
    for (int w = FirstNeighbor(v); w != -1; w = NextNeighbor(v, w)) {
        if (!visited[w]) DFS(w);
    }
}
```

BFS：

```cpp
void BFS(int v) {
    Queue q;
    visited[v] = true;
    EnQueue(q, v);
    while (!Empty(q)) {
        int u = DeQueue(q);
        visit(u);
        for (int w = FirstNeighbor(u); w != -1; w = NextNeighbor(u, w)) {
            if (!visited[w]) {
                visited[w] = true;
                EnQueue(q, w);
            }
        }
    }
}
```

## 手写步骤 / 计算步骤

DFS：访问并标记起点，按邻接点顺序递归深入，无路可走时回退。

BFS：起点入队并标记，队头出队，未访问邻接点依次入队并标记，直到队空。

## 边界条件

非连通图要从每个未访问顶点再次启动遍历。空图无法从指定起点遍历。

## 常见错误

- 忘记 `visited`，导致重复访问。
- BFS 出队才标记，造成重复入队。
- 忽略邻接点顺序。
- 非连通图只遍历一个分量。

## 典型题型

- 写 DFS/BFS 序列。
- 判断遍历能否访问全部顶点。
- 用 BFS 求无权图层次。

## 复杂度分析

邻接矩阵存储下遍历复杂度通常为 `O(n^2)`。邻接表存储下为 `O(n + e)`。

## 与其他知识的联系

DFS 与栈、递归有关；BFS 与队列有关。见 [[Stack_Queue_Basic]]、[[Graph_Adjacency_List]]。

## 相关链接

- [[Graph_Basic]]
- [[Graph_Adjacency_Matrix]]
- [[Graph_Adjacency_List]]
- [[Stack_Queue_Basic]]

## 待追问问题

- DFS 和 BFS 在连通分量统计中如何使用？
- BFS 为什么能求无权图最短边数路径？

## 来源

- knowledge_base/raw/data_structure/graph_dfs_bfs.txt
