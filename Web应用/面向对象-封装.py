# 封装：将属性和方法捆绑在一起，形成一个独立的单元，并隐藏内部的实现细节（私有属性和方法），只对外暴露必要的功能和方法（公共属性和方法）
# 注意，私有的属性和方法只能在类的内部使用；python并没有真正的私有化机制， 约定在私有属性和方法名前加__(两个下划线)
# 强调：封装的目的是隐藏内部实现细节，只对外暴露必要的功能和方法

class Car:
    # 类属性
    wheels = 4  # 轮胎数量
    tax_rate = 0.1 # 税率

    # 构造方法(魔法方法)
    def __init__(self, name, color, owner):
        # 实例属性
        self.name = name
        self.color = color

        self.__owner = '王海淘' # 私有属性(拥有者)

    def start(self):
        print(f"{self.color} {self.name} is starting...")


    def stop(self):
        print(f"{self.color} {self.name} is stopping...")

    def __control_fuel(self):  # 私有方法
        print(f"{self.color} {self.name} is controlling fuel...")

    def get_owner(self):
        return self.__owner[0:1] + '**'  # 返回私有属性


if __name__ == '__main__':
    c1 = Car('保时捷', '白色', '张三')
    c1.start()
    c1.stop()
    print(c1.color)
    print(c1.wheels)
    print(c1.name)
    print(c1.tax_rate)
    print(c1.__owner)  # 报错，私有属性不能被访问
    print(c1.__control_fuel)   # 报错，私有方法不能被访问
    print(c1.get_owner())

    print(c1._Car__owner)   # 访问私有属性
    print(c1._Car__control_fuel())   # 访问私有方法

