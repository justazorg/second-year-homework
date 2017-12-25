#1 написать функцию, которая открывает файл и находит в ней пару "слово-перевод"
#2 заставить функцию проделать эту операцию со всеми файлами в папке
#3 собрать все результаты в один словарь


import re

def open_html(f):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
content = open_html(r'C:\Users\muhni\Desktop\christmas exam\thai_pages\206.6.html')
words = re.findall(r'', content)
print(content)
