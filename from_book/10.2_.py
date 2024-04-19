from pathlib import Path

contents = 'I love programming.\n'
contents += '123\n'
contents += '234\n'

path = Path('programming.txt')
path.write_text(contents)