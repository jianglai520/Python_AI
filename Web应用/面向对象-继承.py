# 注意：私有方法和属性是以__开头的


class Car:
    # 类属性
    wheels = 4  # 轮胎数量
    tax_rate = 0.1 # 税率

    # 构造方法(魔法方法)
    def __init__(self, name, color):
        # 实例属性
        self.name = name
        self.color = color


    def start(self):
        print(f"{self.color} {self.name} is starting...")


    def stop(self):
        print(f"{self.color} {self.name} is stopping...")

    def charge(self):
        print(f"{self.color} {self.name} is charging...")


# 所有类都有父类：object
# 继承：子类继承父类的属性和方法(获取到了父类的非私有的属性和方法)，并添加新的属性和方法
class FuelCar(Car):   # 燃油车
    # 构造方法(魔法方法)
    def __init__(self, name, color, fuel):
        super().__init__(name, color)   #调用父类的构造方法
        self.fuel = fuel    # 燃料

    def charge(self):
        super().charge()  # 方式一
        Car.charge(self)      #方式二：类名.方法名(self)
        print(f"{self.color} {self.name} is charging {self.fuel}")


class ElectricCar(Car):   # 电车
    # 构造方法(魔法方法)
    def __init__(self, name, color, battery):
        super().__init__(name, color)
        self.battery = battery

    # 方法重写
    def charge(self):
        super().charge()   # 方式一：调用父类的方法
        Car.charge(self)   # 方式二：类名.方法名(self)
        print(f"{self.color} {self.name} is charging {self.battery}")



# 测试
if __name__ == '__main__':
    c1 = FuelCar('保时捷', '白色', '汽油')
    c1.start()
    c1.stop()
    print(c1.color)
    print(c1.wheels)
    print(c1.name)
    print(c1.tax_rate)
    print(c1.fuel)
    c1.charge()
    print()

    c2 = ElectricCar('特斯拉', '蓝色', '电')
    c2.start()
    c2.stop()
    print(c2.color)
    print(c2.wheels)
    print(c2.name)
    print(c2.tax_rate)
    print(c2.battery)
    c2.charge()