#读文件

"""
路径写法：
    相对路径：从当前文件所在目录开始查找  -->可移植性强
    .:当前目录  ./可以省略
    ..：上一级目录
    绝对路径：从文件系统的根目录来开始查找,文件位置的完成路径
    方式一：E:\\Python+AI\\file\\秋夕.txt
    方式二：E:/Python+AI/file/秋夕.txt

"""
# with open("./resources/望庐山瀑布.txt",'r', encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# with open("../file/秋夕.txt", 'r', encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# with open("E:\\Python+AI\\file\\秋夕.txt", 'r', encoding="utf-8") as f:   #\ 表示转义符
#     content = f.read()
#     print(content)

with open("E:/Python+AI/file/秋夕.txt", 'r', encoding="utf-8") as f:
    content = f.read()
    print(content)


#追加模式
with open("E:/Python+AI/file/秋夕.txt",'a', encoding="utf-8") as f:
    f.write("追加了一些内容!")