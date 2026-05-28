# Kv Cache

## 1. 核心概念  
KV Cache 是 Transformer 推理阶段的重要优化机制，用于缓存历史 token 的 Key 和 Value，减少重复计算开销。

## 2. 关键流程  
生成新 token 时：  
1. 计算当前 token 的 Query  
2. 读取历史 KV Cache  
3. 与缓存内容进行 Attention 计算  

避免重复计算，显著提升推理速度。

## 3. 误差、优化或实现要点  
- 显存和内存带宽占用问题  
- 缓存数据搬运效率  
- 流水线调度优化  
- memory bandwidth 等关键指标  

## 4. 和硬件/FPGA/加速的关系  
- KV Cache 是推理系统的核心数据流结构  
- 数据搬运、内存带宽、缓存命中率等关键指标  
- FPGA 和 AI Accelerator 需优化 KV Cache 的组织方式  

## 5. 待追问问题  
- KV Cache 的具体实现细节？  
- 如何优化 KV Cache 的内存带宽？  

## 来源  
- knowledge_base/raw/kv_cache.txt