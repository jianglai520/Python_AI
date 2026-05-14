"""
与AI大模型的交互本质是无状态的，想要解决AI大模型会话记忆问题，就要"会话历史滚雪球"
"""


import streamlit as st
import os
from openai import OpenAI
from streamlit import sidebar, session_state
from datetime import datetime
import json

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

#保存会话信息的函数
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 创建seesions 目录不存在则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话数据
        with open("sessions/%s.json" % st.session_state.current_session, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#生成会话标识的函数
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


#加载所有会话列表信息的函数
def load_sessions():
    session_list = []
    # 加载sessions目录下的所有会话文件
    if os.path.exists("sessions"):
        for file in os.listdir("sessions"):
            if file.endswith(".json"):
                session_list.append(file[:-5])
    session_list.sort(reverse=True)      #会话列表,降序排序
    return session_list

#加载指定会话信息
def load_session(session_id):
    try:
        if os.path.exists("sessions/%s.json" % session_id):
            with open("sessions/%s.json" % session_id, "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_id
                st.session_state.messages = session_data["messages"]
    except Exception as e:
        st.error("加载会话失败,请检查会话文件是否正确")

#删除会话信息
def delete_session(session_id):
    try:
        if os.path.exists("sessions/%s.json" % session_id):
            os.remove("sessions/%s.json" % session_id)   #删除文件
            #如果删除的是当前会话，则重新生成会话标识
            if session_id == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_id()
    except Exception as e:
        st.error("删除会话失败!")


# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小园"

# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的西北姑娘"

#会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_id()

# 大标题
st.title("AI智能伴侣")

# 配置logo
st.logo("resources\可爱AI智能伴侣logo设计1.png")

# 左侧的侧边栏
# st.sidebar.subheader("伴侣信息")
# nick_name = st.sidebar.text_input("昵称")
#with是一个上下文管理器，作用是临时改变当前作用域的变量
with st.sidebar:
    # AI控制面板
    st.subheader("AI控制面板")
    #新建会话
    if st.button("新建会话",width = "stretch",icon = "😻"):
        # 1.保存当前会话数据信息
        save_session()
        # 2.创建新的对话
        if st.session_state.messages:  #如果聊天消息非空-->True,反之为False
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()
            save_session()
            st.success("会话创建成功")  # 显示成功信息

    #加载所有会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        # st.button(session, icon = "❤️", width= "stretch")
        # st.button("", icon = "❌", width = "stretch")
        col1, col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            # 三元表达式：条件?真值:假值
            if st.button(session, icon = "❤️", width= "stretch",key=f"load_{session}",type = "primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
        with col2:
            #删除会话信息
            if st.button("", icon = "❌", width = "stretch",key=f"delete_{session}",type = "primary" if session == st.session_state.current_session else "secondary"):
                delete_session(session)

    #分割线
    st.divider()

    #伴侣信息
    st.subheader("伴侣信息")
    #伴侣昵称
    nick_name = st.text_input("昵称", placeholder="请输入伴侣的昵称",value= st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    nature = st.text_area("性格",placeholder="请输入伴侣性格",value= st.session_state.nature)
    if nature:
        st.session_state.nature = nature




#系统提示词
system_prompt = """
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
        """

# 构造与大模型交互的客户端对象(DEEPSEEK_API_KEY环境变量的名字)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

#展示聊天信息
st.text(f"会话名称:{st.session_state.current_session}")
for message in st.session_state.messages:   #["role": "human", "content": prompt}
    # if message["role"] == "human":
    #     st.chat_message("human").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
    st.chat_message(message["role"]).write(message["content"])


#消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:  #字符串会自动转换为布尔值,如果字符串非空--True,否则为False
    st.chat_message("user").write(prompt)
    print("--------> 调用AI大模型,提示词:", prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})


    #调用AI大模型
    # 与大模型进行交互()
    print([
        {"role": "system", "content": system_prompt},
        *st.session_state.messages    #解包
    ])
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt %(st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages    #解包
        ],
        stream=True
    )

    # # 输出大模型返回的结果(非流式输出的解析方式)
    # print("<--------------大模型返回的结果:", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    #输出大模型返回的结果(流式输出的解析方式)
    response_message = st.empty()  # 创建一个空的组件，用于显示大模型返回的结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)


    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    #保存会话信息
    save_session()



