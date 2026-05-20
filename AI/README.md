# AI智能伴侣 - 会话记忆系统

> 一个基于 Streamlit + DeepSeek API 的 AI 对话应用，核心亮点是**会话历史持久化**与**角色扮演系统**

## 🎯 项目概述

本项目是一个具有完整会话管理功能的 AI 对话应用。核心解决了一个关键问题：**AI 大模型的交互本质是无状态的**——通过实现"会话历史滚雪球"机制，让 AI 能够记住上下文，提供连贯的对话体验。

## ✨ 核心功能

### 1. 会话历史持久化
- 自动将会话数据保存为 JSON 文件
- 支持多会话管理，可按时间倒序查看历史
- 会话切换无状态丢失，体验连贯

### 2. 角色扮演系统
- 可自定义 AI 伴侣的**昵称**和**性格**
- 系统提示词动态注入，塑造角色一致性
- 支持 emoji 表情，对话更生动

### 3. 流式响应
- 采用 OpenAI SDK 流式输出
- 打字机效果，提升用户体验

### 4. 会话管理
| 功能 | 说明 |
|------|------|
| 新建会话 | 创建全新对话上下文 |
| 加载历史 | 一键恢复过往会话 |
| 删除会话 | 清理不需要的历史记录 |

## 🛠 技术栈

| 技术 | 用途 |
|------|------|
| **Python** | 后端逻辑 |
| **Streamlit** | 快速构建交互式 Web 界面 |
| **OpenAI SDK** | 对接 DeepSeek API |
| **JSON** | 本地数据持久化 |

## 📁 项目结构

```
.
├── app.py                    # 主程序入口
├── sessions/                 # 会话数据存储目录
│   ├── 2025-01-15_10-30-00.json
│   └── ...
└── resources/                # 静态资源
    └── logo.png
```

## 🔑 核心代码亮点

### 会话保存机制
```python
def save_session():
    session_data = {
        "nick_name": st.session_state.nick_name,
        "nature": st.session_state.nature,
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages
    }
    # 持久化到本地 JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)
```

### 动态系统提示词
```python
system_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色...
伴侣性格：
- %s
"""
# 运行时注入角色参数
messages=[
    {"role": "system", "content": system_prompt % (nick_name, nature)},
    *st.session_state.messages  # 解包历史消息
]
```

### 流式输出处理
```python
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    stream=True  # 启用流式
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        full_response += chunk.choices[0].delta.content
        response_message.chat_message("assistant").write(full_response)
```

## 🚀 运行方式

```bash
# 1. 安装依赖
pip install streamlit openai

# 2. 配置 API Key
set DEEPSEEK_API_KEY=your_api_key_here

# 3. 启动应用
streamlit run app.py
```

## 💡 设计思考

### 为什么做这个项目？

在体验各类 AI 对话产品时，我发现一个痛点：**每次刷新页面，对话上下文就丢失了**。这让我思考——如何让 AI"记住"我们聊过什么？

### 技术选型理由

- **Streamlit**：零前端基础也能快速构建 Web 应用，专注 Python 逻辑
- **JSON 文件存储**：轻量级，无需数据库，适合个人项目
- **DeepSeek API**：国产大模型，性价比高，响应速度快

### 收获与成长

1. **理解了 LLM 的无状态本质**：每次请求都是独立的，必须通过外部存储维护上下文
2. **掌握了状态管理**：使用 `st.session_state` 管理应用状态
3. **体验了全栈开发**：从后端逻辑到前端界面，独立完成完整项目

## 📌 未来优化方向

- [ ] 接入数据库存储（SQLite/PostgreSQL）
- [ ] 支持多用户隔离
- [ ] 增加语音输入/输出功能
- [ ] 引入 RAG 实现知识库问答

---

**项目时间**：2025年  
**开发者**：[你的名字]  
**GitHub**：[你的仓库链接]
