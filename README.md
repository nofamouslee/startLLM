## 大模型学习之旅

目标是脱离ChatGPT网页版，通过编程方式与模型进行交互。

**技术栈**：

- **OpenAI API**: `gpt-4-turbo`, `gpt-3.5-turbo`
- **Anthropic API**: `claude-3-opus/sonnet/haiKu`
- **DeepSeek/智谱AI/Moonshot**等国内优秀模型API
- **Python** `requests` 库或官方SDK



**关键学习点**：

- 如何构造一个有效的API请求（`model`, `messages`, `temperature`, `max_tokens`等参数）。
- 如何处理API响应和解析输出（`content`, `finish_reason`等）。
- 理解`system prompt`和`user prompt`的分工。
- 计算Token和成本控制。



**实践**：

- 写一个Python脚本，分别调用OpenAI和Anthropic的API，询问同一个问题，比较它们的输出风格和逻辑能力。
- 实现一个简单的命令行聊天机器人，可以持续对话并保持上下文（维护`messages`列表）。