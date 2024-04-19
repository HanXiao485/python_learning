from pathlib import Path
import json

number = [2,3,4,5,11,13]

path = Path('number.json')      #将文件对象赋予path
contents = json.dumps(number)   #json.dumps()生成字符串，包含json形式的表达
path.write_text(contents)       #利用.write_text()将上行的表达写入路径