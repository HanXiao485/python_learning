class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")


class Dog(Animal):
    def __init__(self, name, breed):
        super(Dog, self).__init__(name)  # 调用父类的构造函数
        self.breed = breed

    def speak(self):
        return "汪汪！"


my_dog = Dog("旺财", "拉布拉多")
print(my_dog.name)  # 输出："旺财"
print(my_dog.breed)  # 输出："拉布拉多"
print(my_dog.speak())  # 输出："汪汪！"