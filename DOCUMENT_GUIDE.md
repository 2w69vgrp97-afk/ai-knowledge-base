# AI Knowledge Base 使用指南

## 1. 项目目标

本项目用于构建一个轻量级 AI 知识库系统。

它不是普通资料仓库，而是用于把学习过程中形成的理解沉淀为结构化 Wiki。

核心思想是：

raw 原始资料
↓
LLM 编译整理
↓
wiki 结构化知识页
↓
check_wiki.py 质量检查
↓
人工回源修正
↓
持续生长

## 2. 目录说明

### knowledge_base/raw/

用于存放原始资料。

要求：
- 每个 txt 文件只聚焦一个核心概念
- 内容尽量小而清晰
- 不要一次性塞入过多大而全资料
- raw 是事实来源，不应随意被 AI 改写

示例：
- kv_cache_intro.txt
- prefill_decode_intro.txt
- paged_attention_intro.txt

### knowledge_base/wiki/

用于存放 AI 整理后的结构化知识页。

要求：
- 每个页面应包含清晰标题
- 应包含核心概念、关键流程、实现要点、硬件/FPGA/加速关系、待追问问题、来源
- 必须包含“## 来源”部分
- 不确定内容应标注“待核实”

### knowledge_base/outputs/

用于存放临时问答、实验输出、学习过程中的中间结果。

### AGENTS.md

用于规定 AI 维护知识库时必须遵守的规则。

### LINT_REPORT.md

由 check_wiki.py 生成，用于记录知识库质量检查结果。

## 3. 新增知识主题的流程

新增一个主题时，按以下步骤：

1. 先通过提问确认自己是否理解该概念
2. 将理解压缩成一个 raw txt 文件
3. 文件名使用小写英文和下划线，例如：
   kv_cache_intro.txt
   paged_attention_intro.txt
4. 运行：
   python build_wiki.py
5. 运行：
   python check_wiki.py
6. 打开对应 wiki 页面，人工检查是否有：
   - 幻觉
   - 逻辑错误
   - 缺来源
   - 待核实内容
   - 概念混淆
7. 如有问题，回到 raw 对照并修正 wiki

## 4. raw 文件写作原则

raw 文件不是百科复制，而是“知识种子”。

每个 raw 文件应回答一个核心问题。

推荐结构：

- 这个概念是什么
- 为什么需要它
- 它解决了什么问题
- 它和已有知识有什么联系
- 它和硬件/FPGA/系统有什么关系
- 我还不懂什么

不推荐：
- 大段复制网页
- 一个文件塞多个主题
- 只写定义不写原因
- 没有自己的理解

## 5. wiki 页面检查标准

wiki 页面应满足：

- 结构清晰
- 逻辑自洽
- 有来源
- 不凭空编造 raw 中没有的信息
- 不确定内容标注“待核实”
- 能形成知识连接

重点检查：
- compute-bound 和 memory-bound 是否混淆
- Attention / KV Cache / Decode / PagedAttention 的因果链是否正确
- 是否把系统层问题和模型效果问题混在一起

## 6. 当前推荐知识链

当前优先维护这条知识链：

Attention
↓
KV Cache
↓
Prefill / Decode
↓
Continuous Batching
↓
PagedAttention
↓
AI 推理内存管理
↓
FPGA / AI Accelerator 映射

## 7. 后续扩展方向

暂时不要急着加入复杂框架，如 LangChain、Graphify、MCP、多 Agent。

当前优先级是：

1. 理解概念
2. 形成 raw
3. 编译 wiki
4. 检查并修正
5. 建立概念之间的连接

后续可以逐步扩展：
- 自动交叉引用
- 概念关系图
- Obsidian 集成
- 更严格的知识 lint
- 论文资料整理

## 8. Wiki 页面链接规范

每个 wiki 页面尽量包含以下部分，使页面不只是孤立文章，而是知识网络中的节点。

1. `## 前置知识`

用于列出理解本页前最好先掌握的概念。

格式示例：
- [[Band_Theory]]
- [[Crystal_Structure]]

2. `## 相关概念`

用于列出与本页并列、互相影响的概念。

格式示例：
- [[Fermi_Level]]
- [[Carrier_Concentration]]

3. `## 后续影响`

用于列出本页会影响或支撑的后续知识。

格式示例：
- [[PN_Junction]]
- [[MOS_Structure]]

4. `## 核心因果链`

用于写出本页最重要的因果关系。

格式示例：

施主掺杂
↓
费米能级上移
↓
导带电子浓度增加
↓
导电性增强

说明：
- 链接使用 Obsidian 风格 `[[Page_Name]]`
- 暂时不需要实现自动跳转
- 当前阶段只建立文本层面的显式链接
- 不引入向量数据库、LangChain、MCP、多 Agent

## 9. 正文关键词内链规范

正文中出现重要概念时，如果该概念已有对应 wiki 页面，可以使用 Obsidian 风格内链建立跳转关系：

`[[目标文件名|显示文本]]`

例如：
- `[[Band_Theory|能带]]`
- `[[Fermi_Level|费米能级]]`
- `[[Carrier_Concentration|载流子浓度]]`
- `[[Drift_Diffusion|漂移扩散]]`
- `[[PN_Junction|PN结]]`

使用原则：
- 内链用于帮助读者遗忘概念时快速回到解释页
- 同一概念在同一页面首次出现时加链接即可
- 只给核心概念、前置知识、容易遗忘的概念、会影响后续理解的概念加链接
- 不要把整篇文章变成满屏链接
- 链接目标应尽量对应已有 wiki 文件
- 链接应服务于知识关系，而不是装饰
