# 多继承

class Car:
    def __init__(self, brand, model, color, owner):
        self.brand = brand        # 品牌(公有属性)
        self.model = model        # 型号(公有属性)
        self.color = color        # 颜色(公有属性)
        self.__owner = owner      # 拥有者(私有属性)

    def start(self):              # 启动
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self):                # 行驶
        print(f'{self.__owner}: {self.brand} {self.model} 正在行驶...')

    def stop(self):               # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃料...')


# 华为驾驶

class HuaweiDrive():
    def __init__(self, version = 'v1.0'):
        self.version = version

    def run(self):
        print(f"使用华为AI智能驾驶系统{self.version}正在驾驶...")


# 问界
class WenJieCar(Car, HuaweiDrive):
    def __init__(self, brand, model, color, owner, version = 'v1.0'):
        super().__init__(brand, model, color, owner)
        HuaweiDrive.__init__(self, version)

    def run(self):
        super().run()   # 调用父类Car的run方法
        HuaweiDrive.run(self)    # 调用父类HuaweiDrive的run方法
        print(f"使用华为AI智能驾驶系统{self.version}正在驾驶......")

    def charge(self):
        super().charge()
        print(f"使用华为AI智能充电系统{self.version}正在充电...")



if __name__ == '__main__':
    c = WenJieCar("BMW", "X5", "黑色", "张三")
    print(c)
    print(c.__dict__)
    print(WenJieCar.__mro__)   # 查看继承顺序m
    print(WenJieCar.mro())  # 查看继承顺序
    c.run()