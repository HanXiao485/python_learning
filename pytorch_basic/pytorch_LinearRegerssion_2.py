import torch
import matplotlib.pyplot as plt #不加.pyplot报错
from time import perf_counter


def Produce_X(x):
    """拼接矩阵"""
    x0 = torch.ones(x.numpy().size)    #生成与x维度相同的1矩阵
    X = torch.stack((x,x0),dim=1)      #拼接矩阵
    return X                           #返回拼接后的矩阵

# plt.scatter(x.numpy(), y.numpy(), s=0.01)
# plt.show()

def draw(output,loss):
    """绘图函数"""
    if CUDA:
        output = output.cpu()
    plt.cla()                                                                        #清空画布
    plt.scatter(x.numpy(),y.numpy())                                                 #绘制散点原始数据
    plt.plot(x.numpy(),output.data.numpy(),'r-',lw=5)                                #绘制回归直线
    plt.text(0.5,0,'loss = %s' % (loss.item()),fontdict={'size':20,'color':'red'})   #打印loss值
    plt.pause(0.005)


def train(epochs=1 , learning_rate = 0.01):      
    """训练函数"""
    for epoch in range(epochs):
        output = inputs.mv(w)                    #根据现有w值得到输出值，.mv()为矩阵乘法
        loss = (output - traget).pow(2).sum()    #计算当前损失值

        loss.backward()                          #计算当前损失值关于w的梯度向量
        w.data -= learning_rate * w.grad         #更新参数w    （w.data为w中的数据，w.grad为w中的梯度值）
        w.grad.zero_()                           #zero_()清空w的梯度值grad
        if epoch % 80 == 0:
            draw(output,loss)
    return w,loss

#数据输入
x = torch.linspace(-3,3,1000)
X = Produce_X(x)
y = x + 1.2*torch.rand(x.size())
w = torch.rand(2)

#判断GPU
CUDA = torch.cuda.is_available()

if CUDA:
    inputs = X.cuda()
    traget = y.cuda()
    w = w.cuda()
    w.requires_grad = True

else:
    inputs = X
    traget = y
    w = w
    w.requires_grad = True


#输出
start = perf_counter()
w,loss = train(1000,learning_rate=1e-4)
finish = perf_counter()
time = finish - start

print('计算时间:%s'%time)
print('final loss:',loss.item())
print('weights:',w.data)

