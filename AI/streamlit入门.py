import streamlit as st

# st.write("""
# # My first app
# Hello *world*!
# """)

#设置页面配置项
st.set_page_config(
    page_title="Streamlit入门",
    #控制整个网页的内容
    layout="wide",   #centered只占用中间的位置,默认是centered
    #控制侧边栏的状态
    page_icon="🧊",
    initial_sidebar_state="expanded",
    #菜单的信息
    menu_items={
        'Get Help': 'https://www.itcast.cn',
        'Report a bug': "https://www.itcast.cn",
        'About': "#这是一个streamlit的入门程序！"
    }
)

#标题
st.title("Streamlit入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

#段落文字
# st.write("""
# hello!
# """)

st.write("""布偶猫，就像它的名字一样，拥有着如毛绒玩偶般软萌的外表和温顺的性格。

它最令人着迷的是那双湛蓝深邃的眼睛，如同蕴藏着星辰大海的宝石。它身披一身华丽的中长毛，触感如丝般顺滑柔软，身体却结实而富有质感。标志性的重点色——如海豹、蓝色、巧克力色或淡紫色——在它奶油色的身体上晕染开来，优雅而迷人。

布偶猫被称为“小狗猫”，因为它像小狗一样黏人、忠诚。它会热情地迎接你回家，喜欢被抱在怀里，甚至在拥抱时会全身放松、软成一滩，完美契合“布偶”之名。它性情极为温顺，很少发出吵闹的叫声，对孩子和其他宠物也异常宽容，是绝佳的家庭伴侣。

拥有它，就像是把一份会撒娇、会呼噜的温暖棉花糖抱回了家，为你的生活带来无尽的温柔与慰藉。
""")


#图片
# st.image("E:/Python+AI/AI/resources/布偶猫.jpg")
st.image("resources/布偶猫.jpg")

#音频
st.audio("resources/半句再见.mp3")

#视频
st.video("resources/白银市公园.mp4")

#logo
st.logo("resources/logo设计.png")

#表格
#构建字典
student_data = {
    "姓名":["john", "tom", "mars"],
    "年龄":[12, 34, 23],
    "分数":[78, 87, 89]
}
st.table(student_data)


#输入框
name = st.text_input("please input you name!")
st.write(f"your name is {name}")


#密码输入框
password = st.text_input("please input you password!", type="password")
st.write(f"your password is {password}")


#单选按钮
gender = st.radio("请输入您的性别", ['男', '女', '未知'], index=1)
st.write(f"您的性别为{gender}")