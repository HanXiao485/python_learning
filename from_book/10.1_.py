from pathlib import Path

path = Path('pi_digits.txt')

contents = path.read_text()

lines = contents.splitlines()

print(contents)

pi = ''    #定义一个空字符串用于存储
for line in lines:
    pi += line

print(pi)