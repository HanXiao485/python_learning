import torch
import random


x = torch.tensor(list(range(1,11)))
x1 = x.clone().detach()
random.shuffle(x1)

y = torch.tensor(x1[0:3])

z = x[y]

print(x)
print(x1)
print(y)
print(z)
