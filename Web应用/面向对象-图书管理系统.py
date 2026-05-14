"""
# 基于面向对象的编程思想完成如下系统开发

某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。

## 核心功能：

1. 会员登录：会员通过卡号和密码登录系统
2. 借书：会员可以借阅库存中有余量的图书
3. 还书：会员可以归还借阅的图书
4. 查看我的借阅：展示当前会员已经借阅的图书列表
5. 退出系统

## 借阅规则：

1. 普通会员最多可借3本
2. VIP会员最多可借6+VIP等级本（VIP等级，默认为1）

## 注意：

1. 登录成功（卡号和密码均正确）后，才可以访问该系统
2. 图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书

"""

from abc import ABC, abstractmethod
import json


# 定义书籍类
class Book:
    def __init__(self, book_id, title, author,total_num):
        self.book_id = book_id  # 书籍编号
        self.title = title   # 书籍标题
        self.author = author  # 作者
        self.total_num = total_num  # 总数量
        self.__available_num = total_num  # 可借数量(私有属性)

    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    def return_book(self):
        self.__available_num += 1   # 无需判断可用数量>0
        return True

    def get_available_num(self):   # 获取书籍可用数量
        return self.__available_num


# 抽象类:是一种只能被继承，不能被实例化的类---->抽象类不能创建对象,规定子类必须要实现哪些方法，必须遵循通义的代码规范
# 会员类
# python中的抽象类: 使用abc模块定义抽象类 ---> ABC:Abstract Base Class
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员编号
        self.name = name            # 会员姓名
        self.__password = password  # 会员密码
        self.__borrowed_books = []  # 借阅的图书列表

    #定义借书函数
    def borrow_book(self, book:Book):
        # 判断当前会员借阅的数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_borrow_num():
            print("当前会员已借阅了最大数量，无法再借新书")
            return False

        # 判断书籍是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}已经借阅成功")
            return True
        else:
            print("图书库存不足")
            return False



   # 定义还书函数
    def return_book(self, book:Book):
        if book in self.__borrowed_books:   # 判断当前会员是否借阅过该书籍
            book.return_book()
            self.__borrowed_books.remove(book)
            return True
        else:
            print("当前会员没有借阅过该书籍")
            return False

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    # 获取最大借阅数量，需要在子类中实现
    @abstractmethod   # 装饰器，用于检查抽象方法是否被实现
    def get_max_borrow_num(self) -> int:
            pass


# 普通会员类
class NormalMember(Member):
    def get_max_borrow_num(self) -> int:
            return 3


# VIP会员类
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level   # VIP等级


    def get_max_borrow_num(self) -> int:
        return 6 + self.vip_level



# 定义图书馆管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {}   # 存储书籍字典--> {“书籍编号": "Book对象"}
        self.members = {}   # 存储会员列表-->{"会员编号": "Member对象"}
        self.current_member: Member|None = None   # 当前登录的会员
        # 加载数据(书籍和会员的数据)
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        # 加载data/books.json文件
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
               self.books[book['编号']] = Book(book['编号'], book['标题'], book['作者'], book['数量'])
            print("加载书籍数据成功")

    def load_members_data(self):
        with open("data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'].startswith("N"):
                    self.members[member['卡号']] = NormalMember(member['卡号'], member['姓名'], member['密码'])
                elif member['卡号'].startswith("V"):
                    self.members[member['卡号']] = VIPMember(member['卡号'], member['姓名'], member['密码'], member['会员等级'])
            print("加载会员数据成功")

    # 定义登陆函数
    def login(self):
        while True:
            print("【登陆】")
            member_id = input("请输入会员的卡号:")
            password = input("请输入会员的密码:")

            # 判断会员卡号和密码是否存在
            if member_id in self.members and self.members[member_id].get_password() == password:
                self.current_member = self.members[member_id]
                print(f"{self.current_member.name},登录成功, 欢迎您")

                return  True
            else:
                print("会员卡号或密码错误,请重新输入卡号和密码")

                continue
    # 借阅图书
    def borrow_book(self):
        # 展示图书馆的图书列表
        for book in self.books.values():
            print(f"编号:{book.book_id}   标题:{book.title}   作者:{book.author}   可借数量:{book.get_available_num()}")

        # 获取用户输入的图书编号，执行结束操作
        book_id = input("请输入要借阅的图书编号:")
        if book_id not in self.books:
            print("图书编号不存在,借阅失败")
            return
        self.current_member.borrow_book(self.books[book_id])

    # 归还图书
    def return_book(self):
        # 展示当前会员的借阅列表
        for book in self.current_member.get_borrowed_books():
            print(f"编号:{book.book_id}   标题:{book.title}   作者:{book.author}   可借数量:{book.get_available_num()}")

        # 获取用户输入的图书编号，执行结束操作
        book_id = input("请输入要归还的图书编号:")
        if book_id not in self.books:
            print("图书编号不存在,归还失败")
            return
        self.current_member.return_book(self.books[book_id])
        print(f"{self.current_member.name}已经归还成功")

    # 查询借阅列表
    def query_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            for book in borrowed_books:
                print(f"编号:{book.book_id}   标题:{book.title}   作者:{book.author}   可借数量:{book.get_available_num()}")
        else:
            print(f"{self.current_member.name}没有借阅任何图书")

    def run(self):
        if self.login():
            while True:
                print("【图书管理系统】")
                print("\n1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看借阅")
                print("4. 退出系统")
                choice = input("请选择操作(1-4):")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.query_borrowed_books()
                    case "4":
                        print("Goodbye~")
                        break
                    case _:
                        print("无效的选择,请重新选择")



# 测试
if __name__ == '__main__':
    library_system = LibrarySystem()
    library_system.run()










