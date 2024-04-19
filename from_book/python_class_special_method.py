class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# 创建一个类的实例
my_iter = MyIterator([1, 2, 3, 4, 5])

# 使用for循环迭代实例
for item in my_iter:
    print(item)



    