# Prefill Decode Intro

## 1. 核心概念  
- **Prefill**：处理已有输入 token，一次性读取大量 token，主要进行注意力和矩阵乘法运算。  
- **Decode**：生成新 token，需计算当前 token 的 Query，读取历史 KV Cache，依赖上下文长度。  

## 2. 关键流程  
### Prefill  
- **作用**：一次性读取大量 token，利用 GPU 并行计算能力。  
- **优势**：整体更偏向 compute-bound，利用 GPU 利用率高。  

### Decode  
- **流程**：逐个生成新 token，需计算 Query、读取历史 KV Cache、进行注意力计算。  
- **瓶颈**：从 compute-bound 转向 memory-bound，系统瓶颈集中在 memory bandwidth、cache 访问、数据搬运和 pipeline 调度。  

## 3. 误差、优化或实现要点  
### 误差  
- **内存瓶颈**：历史 KV Cache 增大，需频繁搬运数据。  
- **计算效率**：当前仅使用一个 Query，注意力计算方式导致效率下降。  

### 优化  
- **Paged Attention**：优化数据流与内存访问效率。  
- **KV Cache 分页**：减少缓存访问需求。  
- **Continuous Batching**：动态调整 batch size 以平衡资源使用。  

## 4. 和硬件/FPGA/加速的关系  
- **并行度需求**：Prefill 需要高性能 GPU 并行计算能力，Decode 需求优化数据流与内存访问。  
- **缓冲与缓存**：不同阶段对 buffer、cache 的需求不同，需硬件适配。  
- **带宽与调度**：系统瓶颈集中在 memory bandwidth、cache 访问、数据搬运和 pipeline 调度。  

## 5. 待追问问题  
- 如何进一步优化 Decode 的 memory-bound 缓存？  
- FPGA 在 Prefill 和 Decode 中的特殊需求是什么？  

## 来源  
- knowledge_base/raw/prefill_decode_intro.txt