"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：

添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。

修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。

删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。

查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：×××，商品价格：×××，商品数量：×××”。

退出购物车

"""

#定义商品类
class Goods:
    def __init__(self, name, value, num):
        self.name = name
        self.value = value
        self.num = num
    def __str__(self):
        return f"商品名称:{self.name},商品价格:{self.value},商品数量:{self.num}"

    def update_goods(self, name = None, value = None, num = None):
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if num is not None:
            self.num = num

#定义购物车管理系统类
class shoppingCart:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self):
        self.goods = []    #list,记录对应的商品基本信息

    #定义添加购物车
    def add_shopping_cart(self, goods):
        name = input("请输入商品名称:")
        value = input("请输入商品价格:")
        num = input("请输入商品数量:")

        shop_cart = Goods(name, value, num)
        self.goods.append(shop_cart)

    #定义修改购物车
    def change_shopping_cart(self, goods):
        name = input("请输入需要修改的商品名称:")
        for i in self.goods:
            if i.name == name:
                value = input("请重新输入商品的价格")
                num = input("请重新输入商品的数量")
                i.update_goods(name, value, num)
                print("修改成功!")
                print(f"修改后的商品信息为:{i}")
                break
            else:
                print("修改失败，未找到!")
                break

    #定义删除购物车
    def del_shopping_cart(self, goods):
        name = input("请输入商品名称:")
        for i in self.goods:
            if i.name == name:
                self.goods.remove(i)
                print("删除成功")
                print(f"删除货物信息为:{i}")

    #定义查询购物车
    def query_shopping_cart(self, goods):
        for i in self.goods:
            print(i)

    #运行该购物车系统的方法
    def run(self):
        print("欢迎进入购物车管理系统!")
        while True:
            print("------------------------------------")
            print("1.添加购物车信息")
            print("2.修改购物车信息")
            print("3.删除购物车信息")
            print("4.查询购物车信息")
            print("5.退出购物车管理系统")
            print("------------------------------------")
            choice = input("\n请选择要执行的操作,输入1-5:")
            match choice:
                case "1":  # 添加商品
                    self.add_shopping_cart(Goods)
                case "2":  #修改购物车信息
                    self.change_shopping_cart(Goods)
                case "3":  #删除购物车信息
                    self.del_shopping_cart(Goods)
                case "4":  #查询购物车信息
                    self.query_shopping_cart(Goods)
                case "5":  #退出购物车管理系统
                    print("goodbye")
                    break
                case _:  # 其他数字
                    print("输入错误，请选择1-5之间的菜单功能!")

#主函数
if __name__ == "__main__":
    shoppingCart = shoppingCart()
    shoppingCart.run()