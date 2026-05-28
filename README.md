# local_llm_learning

这是一个用于学习 Python 调用本地大模型的最小示例项目。

## 运行步骤

1. 先安装 Ollama

   请前往 Ollama 官网安装适合你系统的版本。

2. 运行 qwen3 模型

   ```bash
   ollama run qwen3
   ```

3. 安装 Python 依赖

   ```bash
   pip install -r requirements.txt
   ```

4. 运行程序

   ```bash
   python app.py
   ```

运行后，在终端中输入你的问题，程序会调用本地 Ollama API 并打印模型回复。
