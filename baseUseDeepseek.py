import os

import openai
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url="https://api.deepseek.com/v1/")

# 最基本的调用deepseek
def baseUser():
    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个乐于助人的编程助手。"},
            {"role": "user", "content": "请用Python写一个函数来计算斐波那契数列。"},
        ],
        temperature=0.7,
        max_tokens=1000
    )

    print(completion.choices[0].message.content)

# 尝试获取模型的思考过程
def reasoning_content():
    completion = client.chat.completions.create(
        model="deepseek-reasoner",  # 使用R1模型
        messages=[
            {'role': 'user', 'content': '9.9和9.11哪个数字更大？'}
        ]
    )

    # 打印思考过程（如果存在）
    if hasattr(completion.choices[0].message, 'reasoning_content'):
        print("思考过程：")
        print(completion.choices[0].message.reasoning_content)

    # 打印最终答案
    print("最终答案：")
    print(completion.choices[0].message.content)

# 流式输出
def StreamingIO():
    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": "详细解释一下Transformer模型的核心机制。"}
        ],
        stream=True,
        max_tokens=2000,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)  # 逐块打印

# 实现多轮对话
def multi_turn_chat():
    conversation_history = [
        {"role": "system", "content": "你是一个幽默的讽刺作家，用百度贴吧暴躁老哥的风格来回答问题。"},
    ]

    # 简单的命令行聊天循环
    print("开始与AI聊天吧！输入 'quit' 或 '退出' 来结束程序。")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ['quit', 'exit', '退出', 'q']:
            print("聊天结束，再会！")
            break

        conversation_history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=conversation_history,
                temperature=0.9,
                # stream=True,
            )

            ai_response = response.choices[0].message.content

            conversation_history.append({"role": "system", "content": ai_response})

        except openai.APIConnectionError as e:
            return f"连接服务器失败: {e}"
        except openai.RateLimitError as e:
            return "请求过于频繁，请稍后再试。"
        except openai.APIStatusError as e:
            return f"OpenAI API返回错误: {e.status_code} - {e.response}"


        print(f"\nAI: {ai_response}")

        # （可选）打印当前对话历史的长度，让你直观看到context在增长
        print(f"[对话轮数: {len(conversation_history) // 2}]")


if __name__ == '__main__':
    multi_turn_chat()