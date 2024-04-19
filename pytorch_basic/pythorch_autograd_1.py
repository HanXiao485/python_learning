import torch

z = torch.ones(2, 1)
X = torch.Tensor([[2, 3], [1, 2]])

X.requires_grad = True

y = X.mm(z)

y.backward(torch.ones(2,1))


print(y)
print(X.grad)