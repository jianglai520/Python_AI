# #读文件
#
# # 1.打开文件
# f = open("resources/望庐山瀑布.txt",'r', encoding="utf-8")
#
# # 2.读取文件内容
# # contents = f.read()   #读取所有内容
# # print(contents)
# content_list = f.readlines()
# for line in content_list:
#     print(line)
#
# # 3.关闭文件
# f.close()


# #写文件
#
# # 1.打开文件
# f = open("resources/静夜思.txt",'w', encoding="utf-8")   #覆盖了原本文件的内容
# # 2.写入文件内容
# f.write("静夜思(李白)\n\n")
# f.write("窗前明月光，\n")
# f.write("玉盘\n")
# f.write("西风瘦马，\n")
# f.write("西风瘦马，\n")
# # 3.关闭文件-->释放文件资源
# f.close()


#释放资源-----方式1-----------------
# f = open("resources/静夜思.txt",'w', encoding="utf-8")
# try:
#
#     f.write("静夜思(李白)\n")
#     f.write("窗前明月光，\n")
#     i = 1 / 0
#     f.write("疑是地上霜，\n")
#
# finally:
#     print("关闭文件")
#     f.close()

#释放资源-----方式2(推荐方式)-----------------
with open("resources/静夜思.txt",'w', encoding="utf-8") as f:
    f.write("静夜思(李白)\n")
    f.write("窗前明月光，\n")
    i = 1 / 0
    f.write("疑是地上霜，\n")
    print("关闭文件")
