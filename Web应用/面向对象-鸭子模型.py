# 鸭子模型

class Duck:  # 1个用法

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动 1个用法
        print(f'Duck {self.age} 岁的 {self.name} 正在游泳...')


class Dog:  # 1个用法

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Dog {self.age} 岁的 {self.name} 正在游泳...')


class Pig:  # 1个用法

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Pig {self.age} 岁的 {self.name} 正在游泳...')


def go_swimming(animal):  # 1个用法
      animal.swimming()  # 启动


if __name__ == '__main__':
    duck = Duck('小黄鸭', 1)
    dog = Dog('小黄狗', 2)
    pig = Pig('小黄猪', 3)
    go_swimming(duck)
    go_swimming(dog)
    go_swimming(pig)