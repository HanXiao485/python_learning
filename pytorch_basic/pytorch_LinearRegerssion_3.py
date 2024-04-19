import torch
import matplotlib.pyplot as plt
from torch import nn,optim
from time import perf_counter

x = torch.unsqueeze(torch.linspace(-3,3,1000),dim=1)  #.unsqueeze在第一维增加一个维度
y = x+1.2*torch.rand(x.size())

class LR(nn.Module):
    def __init__(self):
        super(LR,self).__init__()
        self.linear = nn.Linear(1,1)

    def forward(self,x):
        out = self.linear(x)
