from pathlib import Path
import json

path = Path('number.json')     #指定路径
contents = path.read_text()    #用read_text()的方法，读取该路径下的文件
number = json.loads(contents)  #将json文件的内容转化为字符串赋予number

print(number)