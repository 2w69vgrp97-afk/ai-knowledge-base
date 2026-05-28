# Prefill Decode  

## 1. 核心概念  
- **Prefill**：用于一次性读取输入 token，处理过程中同时进行注意力和矩阵乘法计算。  
- **Decode**：基于已生成部分 token，逐个生成新 token，依赖当前 token 的 Query、历史 KV Cache 和历史 Key 进行注意力计算。  

## 2. 关键流程  
- **Prefill**：一次性读取大量 token，计算过程中需处理大量矩阵运算，GPU 可以并行调用大量核心以提高效率。  
- **Decode**：逐个生成新 token，计算过程中需处理当前 Query、历史 KV Cache 和历史 Key 的注意力。  

## 3. 误差、优化或实现要点  
- **误差**：Decode 阶段可能因历史 KV Cache 大而内存带宽不足，导致瓶颈集中在内存访问、缓存和数据搬运。  
- **优化**：  
  - Paged Attention：优化数据流和内存访问效率。  
  - KV Cache 分页：减少内存带宽和缓存访问压力。  
  - Continuous Batching：动态调整批次以平衡内存和计算需求。  

## 4. 和硬件/FPGA/加速的关系  
- **Prefill**：对并行度、缓冲、缓存、带宽和管道需求较高。  
- **Decode**：对并行度、缓冲、缓存、带宽和管道需求较低。  

## 5. 待追问问题  
- 如何平衡 Prefill 和 Decode 的并行需求？  
- FPGA 在 Prefill 和 Decode 中的优化策略？  

## 来源  
- knowledge_base/raw/ai_inference/prefill_decode.txt