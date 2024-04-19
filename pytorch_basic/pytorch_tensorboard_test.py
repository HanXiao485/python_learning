import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter

# 创建一个模拟的神经网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, 1)

    def forward(self, x):
        x = self.fc1(x)
        return x

# 准备数据
x_train = torch.tensor([[1.], [2.], [3.], [4.], [5.]])
y_train = torch.tensor([[2.], [4.], [6.], [8.], [10.]])

# 创建模型、损失函数和优化器
model = Net()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 创建 TensorBoard 的 SummaryWriter 对象
writer = SummaryWriter()

# 训练模型，并将指标写入 TensorBoard
for epoch in range(100):
    optimizer.zero_grad()
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    loss.backward()
    optimizer.step()

    # 将损失值写入 TensorBoard
    writer.add_scalar('Loss/train', loss, epoch)

# 关闭 SummaryWriter 对象
writer.close()
