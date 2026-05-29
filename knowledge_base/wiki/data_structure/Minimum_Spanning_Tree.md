# Minimum Spanning Tree

## 核心概念

最小生成树 MST 是无向连通带权图中，连接全部顶点且总权值最小的生成树。

Prim 从点集扩展：每次选连接集合内外的最小权边。

Kruskal 从边集选择：按边权从小到大选边，不能形成回路。

MST 可能不唯一，但最小总权值相同。

## 考试识别信号

- 求最小生成树或最小代价。
- 写 Prim 或 Kruskal 选边顺序。
- 图是无向带权连通图。

## 核心公式 / 代码模板

生成树边数：`n - 1`。

MST 适用前提：无向、连通、带权图。

## 手写步骤 / 计算步骤

Prim：

1. 任选起点加入集合 `U`。
2. 从连接 `U` 和 `V-U` 的边中选最小权边。
3. 将新顶点加入 `U`。
4. 重复直到所有顶点加入。

Kruskal：

1. 边按权值从小到大排序。
2. 依次检查边。
3. 不成环则加入 MST。
4. 选够 `n - 1` 条边结束。

## 边界条件

图不连通时不存在覆盖全部顶点的生成树，只能得到最小生成森林。单顶点图 MST 边数为 0。

## 常见错误

- 在有向图上求 MST。
- 忘记必须连通。
- Kruskal 不判断成环。
- 认为 MST 一定唯一。

## 典型题型

- 手算 Prim 选边过程。
- 手算 Kruskal 选边过程。
- 判断多个 MST 是否可能。

## 复杂度分析

考试手算通常关注选边过程。具体实现复杂度与图存储结构、排序和并查集实现有关。

## 与其他知识的联系

MST 基于 [[Graph_Basic]]。Prim 常配合 [[Graph_Adjacency_Matrix]]，Kruskal 常需要按边排序和判环。

## 相关链接

- [[Graph_Basic]]
- [[Graph_Adjacency_Matrix]]
- [[Graph_Adjacency_List]]
- [[Sort_Complexity_Stability_Summary]]

## 待追问问题

- Kruskal 中并查集如何判断成环？
- Prim 从不同起点是否会得到不同 MST？

## 来源

- knowledge_base/raw/data_structure/minimum_spanning_tree_prim_kruskal.txt
