#例2-1-3 利用自动微分和优化器求最小值
import numpy as np
import torch
 
# f(x) = a*x**2 + b*x + c的最小值
x = torch.tensor(0.0, requires_grad=True)  # x需要被求导
a = torch.tensor(1.0)
b = torch.tensor(-2.0)
c = torch.tensor(1.0)
optimizer = torch.optim.SGD(params=[x], lr=0.01)  #SGD为随机梯度下降
print(optimizer)
 
def f(x):
    result = a * torch.pow(x, 2) + b * x + c
    return (result)
 
for i in range(500):
    optimizer.zero_grad()  #将模型的参数初始化为0
    y = f(x)
    y.backward()  #反向传播计算梯度
    optimizer.step()  #更新所有的参数
print("y=", y.data, ";", "x=", x.data)