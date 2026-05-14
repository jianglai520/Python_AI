# 同一个方法具有不同的形态--->可以增强扩展性

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


# 继承：子类继承父类的属性和方法(获取到了父类的非私有的属性和方法)，并添加新的属性和方法
class FuelCar(Car):   # 燃油车
    def charge(self):
        print(f"{self.color} {self.model} is charging...")


class ElectricCar(Car):   # 电车
    def charge(self):
        print(f"{self.color} {self.model} is charging.....")


# 补充燃料函数
def handle_charge(car: Car):   # 函数参数类型声明--指定的是父类型
    car.charge()

# 测试
if __name__ == '__main__':
    handle_charge(FuelCar('保时捷', 'X5', '黑色', '张三'))
    handle_charge(ElectricCar('特斯拉', 'han', '黑色', '张三'))