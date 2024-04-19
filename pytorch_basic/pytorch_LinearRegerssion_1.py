import torch
import matplotlib.pyplot as plt #不加.pyplot报错

def Produce_X(x):
    """拼接矩阵"""
    x0 = torch.ones(x.numpy().size)    #生成与x维度相同的1矩阵
    X = torch.stack((x,x0),dim=1)      #拼接矩阵
    print(torch.stack((x,x0),dim=1).shape)
    print(torch.stack((x,x0),dim=1))
    return X                           #返回拼接后的矩阵

def train(epochs=1 , learning_rate = 0.01):      
    """训练函数"""
    for epoch in range(epochs):
        output = inputs.mv(w)                    #根据现有w值得到输出值
        loss = (output - traget).pow(2).sum()    #计算当前损失值

        loss.backward()                          #计算当前损失值关于w的梯度向量
        w.data -= learning_rate * w.grad         #更新参数w    （w.data为w中的数据，w.grad为w中的梯度值）
        w.grad.zero_()                           #zero_()清空w的梯度值grad
        if epoch % 80 == 0:
            draw(output,loss)
    return w,loss

def draw(output,loss):
    """绘图函数"""
    plt.cla()                                                                        #清空画布
    plt.scatter(x.numpy(),y.numpy())                                                 #绘制散点原始数据
    plt.plot(x.numpy(),output.data.numpy(),'r-',lw=5)                                #绘制回归直线
    plt.text(0.5,0,'loss = %s' % (loss.item()),fontdict={'size':20,'color':'red'})   #打印loss值
    plt.pause(0.005)


x = torch.Tensor([1.3 , 5 , 11 , 16 , 21])
y = torch.Tensor([14.4 , 29.6 , 62 , 85.5 , 113.4])
X = Produce_X(x)

inputs  = X
traget = y
w = torch.rand(2,requires_grad=True)   #随即生成初始化参数向量w，利用梯度下降进行更新

w,loss = train(10000,learning_rate=1e-4)

print('final loss',loss.item())
print('weights:',w.data)
print('weights:',w)



# plt.scatter(x.numpy() , y.numpy())
# plt.show()
