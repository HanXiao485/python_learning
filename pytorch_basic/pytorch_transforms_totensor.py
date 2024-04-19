from PIL import Image
from torchvision import transforms

img_tool = transforms.ToTensor()
img_path = 'D:\BIT(master)\python\python learning\pic\/2018America.jpg'    #利用/进行2018的转译
img = Image.open(img_path)

out_put = img_tool(img)

print(img)
print(out_put)