from sklearn.preprocessing import OneHotEncoder
import torch
import torchvision 
import pandas as pd
import numpy as np
import os
import torch.nn as nn
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split

encoder = OneHotEncoder(sparse_output=False)

data = pd.read_csv('titanic\\train.csv')    #载入csv文件

x1 = data['Age']                           #提取年龄信息
x1 = x1.fillna(1).tolist()                 #用replacement_value替换NaN值并转换为列表

x2 = data['Sex']                           #提取性别信息
label_map = {"male": 0, "female": 1}       #将性别编码
x2 = [label_map[label] for label in x2]

x3 = data['Pclass']

y = data['Survived']                       #提取存活信息


data_age = torch.tensor(x1,dtype=torch.float32)
data_sex = torch.tensor(x2,dtype=torch.float32)
data_pclass = torch.tensor(x3,dtype=torch.float32)
data_input = torch.stack((data_age,data_sex,data_pclass),dim=1)

data_sur = torch.tensor(y,dtype=torch.float32)



class titanic(Dataset):
    '''数据集处理'''
    def __init__(self,input,sur):
        self.input = input
        self.sur = sur

    def __len__(self):
        return len(self.sur)

    def __getitem__(self, idx):
        return self.input[idx], self.sur[idx]


class Model(nn.Module):
    '''定义训练模型'''
    def __init__(self) -> None:
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(3,4),
            nn.Linear(4,3),
            nn.Linear(3,2),
            nn.Linear(2,1),
        )
    def forward(self,x):
        return self.model(x)
    


#切分原始数据集 分为 训练集 测试集
input_train, input_test, sur_train, sur_test = train_test_split(data_input, data_sur, test_size=0.2, random_state=42)

dataset_train = titanic(input_train, sur_train)
dataset_test = titanic(input_test, sur_test)

train_loader = DataLoader(dataset=dataset_train, batch_size=40, shuffle=True,drop_last=True)
test_loader = DataLoader(dataset=dataset_test, batch_size=40, shuffle=False,drop_last=True)


model = Model()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
losses = []


for epoch in range(300):
    for i, data0 in enumerate(train_loader):
        input,data1 = data0     #获得数据 data0中包含input, target

        output = model(input)   #利用模型进行计算

        loss = criterion(output, data1)     #计算损失
        optimizer.zero_grad()

        loss.backward()                     #反向求导
        optimizer.step()                    #更新优化器参数

    losses.append(loss.item())              #将loss值存入列表 画图

    #读取模型参数！！！！！！
    for name, param in model.named_parameters():
        print(f"Parameter name: {name}")
        print(f"Parameter value: {param.data}")

    print(f'epoch:{epoch}, loss:{loss.item()}\n')


plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()



#测试模型
model.eval()  # 将模型设置为评估模式

mse = 0.0
num_samples = 0

with torch.no_grad():
    for data in test_loader:
        inputs, targets = data
        outputs = model(inputs)
        mse += ((outputs - targets) ** 2).sum().item()
        num_samples += len(inputs)

mse /= num_samples

print(f"Mean Squared Error on test set: {mse}")

        


