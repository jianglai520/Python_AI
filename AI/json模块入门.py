#写入json数据文件
import json

#写入json数据文件
user = {
    "name": "小园",
    "age": 18,
    "gender": "女",
    "hobby": ["看电影", "听音乐", "看小说"]
}


#将python对象写入json文件
# with open("resources/user.json",'w', encoding="utf-8") as f:
#     json.dump(user, f, ensure_ascii=False,indent = 2)   #ensure_ascii=False, 保存中文(非ASCII保留原样输出);indent, 缩进(格式化)



#读取json数据文件
with open("resources/user.json",'r', encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))