# Paged Attention  
## 1. 核心概念  
PagedAttention 是一种用于管理 Transformer KV Cache 的机制，通过将用户的 KV Cache 拆分成多个 page/block，实现以下特点：  
- 用户的 KV 不需连续存储，减少显存碎片化  
- 系统可动态调度 KV Cache，提高资源利用率  
- 上下文增长时仅需新增 page，减少数据搬运量  

## 2. 关键流程  
### 1.1 用户 KV Cache 拆分  
- 将用户的 KV Cache 分为多个 page/block  
- 用户的 KV 不需连续存储，实现内存优化  
- 系统通过 page table 记录映射关系，实现动态调度  

### 1.2 显存利用提升  
- 显存利用率提高，减少碎片化问题  
- 批量处理能力增强，支持连续数据流  

### 1.3 动态调度能力  
- 上下文增长时只需新增 page，减少数据搬运  
- 无需整体搬运 KV Cache  

## 3. 误差、优化或实现要点  
### 3.1 误差  
- 显存碎片化问题，需动态管理 KV Cache 的分配  

### 3.2 优化  
- 通过 page table 实现动态调度  
- 显存利用率提升，减少整体搬运量  

## 4. 和硬件/FPGA/加速的关系  
### 4.1 Page size 设计考量  
- 内存对齐：确保缓存访问的原子性  
- 缓存局部性：减少数据重复访问  
- GPU 数据读取效率：优化内存访问模式  

## 5. 待追问问题  
- 如何优化 Page size 的分配策略？  
- 当内存对齐不足时，如何处理？  
- 实现动态调度的具体方法是什么？  

## 来源  
- knowledge_base/raw/ai_inference/paged_attention.txt