 
import torch

# 假设是时间步T1的输出
T1 = torch.tensor([[1, 2, 3]])
# 假设是时间步T2的输出
T2 = torch.tensor([[10, 20, 30]])

print(torch.stack((T1,T2),dim=0).shape)
print(torch.stack((T1,T2),dim=1).shape)
#print(torch.stack((T1,T2),dim=2).shape)
print(torch.stack((T1,T2),dim=0))
print(torch.stack((T1,T2),dim=1))
#print(torch.stack((T1,T2),dim=2))
#print(torch.stack((T1,T2),dim=3).shape)
# outputs:
torch.Size([2, 3, 3])
torch.Size([3, 2, 3])
torch.Size([3, 3, 2])


