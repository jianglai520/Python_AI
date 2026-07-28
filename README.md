<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-green?logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/DeepSeek-API-4F46E5?logo=deepseek" alt="DeepSeek">
</p>

<h1 align="center">Python + AI 入门学习之旅</h1>

<p align="center">
  <strong>从 Python 基础语法到 AI 应用开发的全栈学习笔记</strong>
  <br>
  基础语法 -> 面向对象 -> AI 应用 -> 数据分析 -> 网络爬虫 -> Web 开发
</p>

---

## 项目简介

**Python+AI** 是一套完整的 Python 学习笔记与实践项目合集，记录了从编程入门到 AI 应用开发的全过程。项目涵盖 Python 基础语法、面向对象编程、数据分析、网络爬虫、Web 开发（FastAPI/Streamlit）以及 AI 大模型集成等核心领域。

> 核心理念："与AI大模型的交互本质是无状态的"——通过"会话历史滚雪球"机制，让 AI 记住上下文。

---

## 项目结构

```
Python+AI/
+-- 基础语法/                    # Python 基础与面向对象
|   +-- 教务管理系统-面向对象.py   # 教务管理系统（CRUD）
|   +-- 购物管理系统--面向对象.py  # 购物管理系统
|   +-- 异常处理.py
|   +-- 异常传递.py
|
+-- AI/                          # AI 应用开发
|   +-- ai智能伴侣.py             # AI 智能伴侣（Streamlit + DeepSeek）
|   +-- deepseek调用测试.py       # DeepSeek API 调用测试
|   +-- streamlit入门.py          # Streamlit 框架入门
|   +-- datetime入门.py
|   +-- json模块入门.py
|   +-- 文件操作入门/扩展.py
|   +-- sessions/                 # 会话数据（JSON）
|   +-- resources/                # 图片/音频/视频资源
|   +-- README.md                 # AI 模块文档
|
+-- Web应用/                     # Web 开发
|   +-- fastapi入门.py            # FastAPI 入门
|   +-- 面向对象-封装/继承/多态.py # OOP 系列
|   +-- 面向对象-图书管理系统.py  # 图书管理系统（完整 OOP 项目）
|   +-- data/                    # JSON 数据文件
|   +-- 汉字谜盒/                 # 汉字谜盒 Web 应用
|       +-- main.py              # FastAPI 后端
|       +-- static/              # 前端文件
|       +-- sessions/
|
+-- 数据分析/                    # 数据分析
|   +-- pandas入门.ipynb
|   +-- Series入门.ipynb
|   +-- DataFrame入门演示.ipynb
|   +-- matplotlib入门/实战.ipynb
|   +-- 数据分析实战.ipynb       # TMDB 电影数据分析
|   +-- 数据分析实战.py          # 脚本版
|   +-- data/
|       +-- movies.csv           # TMDB TOP300 数据
|       +-- sales.csv
|       +-- movies_statistics.png
|
+-- 网络机器人/                  # 网络爬虫
|   +-- 网络机器人入门.py        # TIOBE 排行榜爬虫
|   +-- 网络机器人案例.py        # TMDB 电影榜单爬虫
|   +-- Xpath语法演示.py
|   +-- 正则表达式入门.py
|   +-- 网页解析入门.py
|   +-- 电影榜单.csv
|
+-- file/                        # 文本文件
+-- 学习截图/                    # 70+ 张学习截图
+-- .idea/                       # PyCharm 配置
+-- README.md                    # 本文件
```

---

## 学习路线

| 阶段 | 内容 | 核心项目 |
|------|------|---------|
| 第1阶段 基础语法 | 异常处理、编程思维 | 算法练习题 |
| 第2阶段 面向对象 | 封装/继承/多态/抽象类 | 教务管理、图书管理、购物系统 |
| 第3阶段 AI 应用 | DeepSeek API、Streamlit、FastAPI | AI 智能伴侣、汉字谜盒 |
| 第4阶段 数据分析 | Pandas、Matplotlib、Jupyter | TMDB TOP300 电影数据分析 |
| 第5阶段 网络爬虫 | requests、lxml、XPath、正则 | TIOBE 排行榜、TMDB 电影榜单 |
| 第6阶段 Web 开发 | FastAPI、前后端交互 | 汉字谜盒（完整前后端） |

---

## 核心项目亮点

### 1. AI 智能伴侣

基于 **Streamlit + DeepSeek API** 的 AI 对话应用：

| 特性 | 说明 |
|------|------|
| 会话记忆 | JSON 持久化历史聊天，解决 LLM 无状态问题 |
| 角色扮演 | 昵称+性格动态注入 System Prompt |
| 流式输出 | 打字机效果实时展示 |
| 多会话管理 | 新建/加载/删除 |

核心设计——"会话历史滚雪球"：
```python
messages = [
    {"role": "system", "content": system_prompt % (nick_name, nature)},
    *st.session_state.messages  # 解包历史消息
]
```

### 2. 图书管理系统（OOP 设计）

| 设计模式 | 实现 |
|---------|------|
| 抽象基类 (ABC) | Member 定义借书/还书接口 |
| 继承 | NormalMember / VIPMember 不同权限 |
| 封装 | 私有属性 password、borrowed_books |
| 多态 | 不同车辆充电行为 |
| 持久化 | JSON 加载书籍和会员数据 |

### 3. TMDB 电影分析（完整 pipeline）

1. 爬虫：requests + lxml 爬取 TOP300（分页+详情页）
2. 清洗：Pandas 处理缺失值
3. 分析：年份趋势/语言分布/类型分布/评分占比
4. 可视化：Matplotlib 四子图

### 4. 汉字谜盒

基于 **FastAPI + DeepSeek** 的 Web 字谜游戏：
- 三栏布局、暗黑/明亮主题
- 70+ 行 System Prompt 确保出题质量
- 完整的会话管理

---

## 快速使用

```bash
# 安装依赖
pip install openai streamlit fastapi uvicorn pandas matplotlib jupyter requests lxml

# 设置 API Key
export DEEPSEEK_API_KEY="your-api-key-here"

# 运行各模块
streamlit run AI/ai智能伴侣.py                           # AI 智能伴侣
python "Web应用/汉字谜盒/main.py"                        # 汉字谜盒
jupyter notebook 数据分析/                                 # 数据分析
python 网络机器人/网络机器人案例.py                        # 网络爬虫
python Web应用/面向对象-图书管理系统.py                    # 图书管理系统
```

---

## 技术栈

| 类别 | 技术 |
|------|------|
| 编程语言 | Python 3.10+ |
| AI 大模型 | DeepSeek Chat（OpenAI SDK） |
| Web 框架 | FastAPI / Streamlit |
| 数据分析 | Pandas、Matplotlib、Jupyter |
| 网络爬虫 | requests、lxml、XPath |
| 数据存储 | JSON 文件 |

---

## 后续计划

- 接入 SQLite/PostgreSQL 数据库
- 支持更多 AI 模型（通义千问、GLM）
- 异步爬虫（aiohttp）
- FastAPI + Vue3 前后端分离
- Docker 容器化部署

---

<p align="center">
  <sub>基础语法 -> 面向对象 -> AI 大模型 -> 数据分析 -> 爬虫 -> Web 开发</sub>
</p>
