# csv操作

# 方式一,pycharm可以直接识别csv文件--文件操作的原始方式
# with open("csv_data/01.csv", "w", encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")  # 写入表头
#     f.write("小王,18,男,'python,c'\n")   # 写入数据
#     f.write("小张,19,女, java\n")
#     f.write("小李,20,男, go\n")

# # 读数据
# with open("csv_data/01.csv", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())
#
# # 方式二：csv模块
import csv

# with open("csv_data/02.csv", "w", encoding="utf-8", newline = "") as f:   # newline = "" 表示不添加换行符
#     writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
#     writer.writeheader()  # 写入表头
#     writer.writerow({"姓名": "小王", "年龄": 18, "性别": "男", "爱好": "python,c"})
#     writer.writerow({"姓名": "小张", "年龄": 19, "性别": "女", "爱好": "java"})
#     writer.writerow({"姓名": "小李", "年龄": 20, "性别": "男", "爱好": "go"})  # 写入数据

# 读数据
with open("csv_data/02.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)   # 输出的是dict格式
        print(line["姓名"], line["年龄"], line["性别"], line["爱好"])