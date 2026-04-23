"""
与AI大模型的交互本质是无状态的，想要解决AI大模型会话记忆问题，就要"会话历史滚雪球"
"""


import streamlit as st
import os
from openai import OpenAI

print("------------>重新执行文件")

#设置页面配置项
st.set_page_config(
    page_title="AI智能伴侣",
    #控制整个网页的内容
    layout="wide",   #centered只占用中间的位置,默认是centered,wide是占满整个区域
    #控制侧边栏的状态
    page_icon="😊",
    initial_sidebar_state="expanded",
    #菜单的信息
    menu_items={}
)

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 大标题
st.title("AI智能伴侣")

#配置logo
st.logo("resources\可爱AI智能伴侣logo设计1.png")

#系统提示词
system_prompt = "You are a helpful assistant,you name is 园园"

# 构造与大模型交互的客户端对象(DEEPSEEK_API_KEY环境变量的名字)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

#展示聊天信息
for message in st.session_state.messages:   #["role": "human", "content": prompt}
    # if message["role"] == "human":
    #     st.chat_message("human").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
    st.chat_message(message["role"]).write(message["content"])


#消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:  #字符串会自动转换为布尔值,如果字符串非空--True,否则为False
    st.chat_message("human").write(prompt)
    print("--------> 调用AI大模型,提示词:", prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "human", "content": prompt})


    #调用AI大模型
    # 与大模型进行交互()
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content":prompt},
        ],
        stream=False
    )

    # 输出大模型返回的结果
    print("<--------------大模型返回的结果:", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})



