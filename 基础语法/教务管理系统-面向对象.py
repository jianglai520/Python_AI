#面向对象思想方法--完成教务管理系统的基本开发
#分析：student(属性和方法), EduMangement(manage学生)

"""
添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
1.3 验证成绩范围（0-100分）
1.4 创建学生对象并添加到系统

修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
2.1 输入要修改的学生姓名
2.2 根据姓名查找该学生，显示该生当前成绩信息
2.3 输入新的语文、数学、英语成绩
2.4 更新学生成绩数据

删除学生成绩：根据输入的学生姓名，删除对应的学生成绩

查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
4.1 输出格式为："姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
展示全部学生成绩：展示出系统中所有学生的成绩

"""

#定义学生类
class Student:
    def __init__(self,name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    #输出格式为："姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math}| 英语：{self.english} | 总分：{self.chinese+self.math+self.english}"

    #修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):  #设置默认值None
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


#定义教务管理系统的类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []         #列表，记录在校学生的成绩信息

    #添加学生成绩
    def add_score(self, Student):
        name = input("请输入学生的姓名:")
        #判断学生姓名是否存在,如果存在,则添加失败(不能重复添加)
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在,添加失败!")
                break   #return也可

        chinese = int(input("请输入学生的语文成绩:"))
        math = int(input("请输入学生的数学成绩:"))
        english = int(input("请输入学生的英语成绩:"))

        #判断分数输入是否合适(0-100)
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("学生信息添加成功!")
        else:
            print("成绩输入有误!请重新输入0~100范围内的成绩!")

    #修改学生成绩
    def update_score(self):
        name = input("请输入要修改的学生姓名:")

        #根据学生姓名找到该学生的信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩是:{s}")
            chinese = int(input("请输入学生修改后的语文成绩:"))
            math = int(input("请输入学生修改后的数学成绩:"))
            english = int(input("请输入学生修改后的英语成绩:"))

            # 判断分数输入是否合适(0-100)
            if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                s.update_score(chinese, math, english)
                print("成绩修改成功")
                print(f"修改后的成绩是:{s}")
                break

            else:
                print("成绩输入有误!请重新输入0~100范围内的成绩!")
                break

        print("未找到该学生，修改失败!")

    #删除学生成绩
    def del_score(self):
        name = input("请输入要删除的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功!")
                break
        print("未找到该学生，删除失败!")


    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询学生的姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                break
        print("为找到该学生，查询失败!")

    #展示所有学生成绩
    def display_student(self):
        for s in self.student_list:
            print(s)

    #运行系统的方法
    def run(self):
        print(f"欢迎使用教务管理系统,当前教务系统版本为{EduManagement.system_version}")

        while True:
            print()
            print("----------------------------------------")
            print("1.添加学生")
            print("2.修改学生")
            print("3.删除学生")
            print("4.查询指定学生")
            print("5.查询所有学生")
            print("6.退出当前教务管理系统")
            print("----------------------------------------")

            choice = input("\n请选择要执行的操作,输入1-6:")
            try:
                match choice:
                    case "1": #添加学生
                        self.add_score(Student)
                    case "2":
                        self.update_score()
                    case "3":
                        self.del_score()
                    case "4":
                        self.query_student()
                    case "5":
                        self.display_student()
                    case "6":
                        print("goodbye")
                        break
                    case _:  #其他数字
                        print("输入错误，请选择1-6之间的菜单功能!")
            except ValueError as e:
                print("输入的数据有问题，请检查并重新输入", e)
            except Exception:
                print("程序运行出错了，请重新选择~")

#主函数
if __name__ == "__main__":
    manage = EduManagement()
    manage.run()










