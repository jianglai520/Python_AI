class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def run(self):
        print('%s %s is running...' % (self.color, self.name))

    def total_cost(self, discount, rate = 0.1):
        total_cost = self.price * (1 - discount - rate)
        return total_cost


# 测试
c1 = Car('保时捷', '白色')
c1.run()