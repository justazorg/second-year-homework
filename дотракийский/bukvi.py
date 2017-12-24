import re
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


def open_html(f):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
content = open_html(r'C:\Users\muhni\Desktop\дотракийский\словарик.html')
a = re.findall(r'id="a\w+"', content)
b = re.findall(r'id="b\w+"', content)
c = re.findall(r'id="c\w+"', content)
d = re.findall(r'id="d\w+"', content)
e = re.findall(r'id="e\w+"', content)
f = re.findall(r'id="f\w+"', content)
g = re.findall(r'id="g\w+"', content)
h = re.findall(r'id="h\w+"', content)
i = re.findall(r'id="i\w+"', content)
j = re.findall(r'id="j\w+"', content)
k = re.findall(r'id="k\w+"', content)
l = re.findall(r'id="l\w+"', content)
m = re.findall(r'id="m\w+"', content)
n = re.findall(r'id="n\w+"', content)
o = re.findall(r'id="o\w+"', content)
p = re.findall(r'id="p\w+"', content)
q = re.findall(r'id="q\w+"', content)
r = re.findall(r'id="r\w+"', content)
s = re.findall(r'id="s\w+"', content)
t = re.findall(r'id="t\w+"', content)
u = re.findall(r'id="u\w+"', content)
v = re.findall(r'id="v\w+"', content)
w = re.findall(r'id="w\w+"', content)
x = re.findall(r'id="x\w+"', content)
y = re.findall(r'id="y\w+"', content)
z = re.findall(r'id="z\w+"', content)
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Y = [len(a), len(b), len(c), len(d), len(e), len(f), len(g), len(h), len(i), len(j), len(k), len(l), len(m), len(n), len(o), len(p), len(q), len(r), len(s), len(t), len(u), len(v), len(w), len(x), len(y), len(z)]

print ('Всего слов на "А":', len(a))
print ('Всего слов на "B":', len(b))
print ('Всего слов на "C":', len(c))
print ('Всего слов на "D":', len(d))
print ('Всего слов на "E":', len(e))
print ('Всего слов на "F":', len(f))
print ('Всего слов на "G":', len(g))
print ('Всего слов на "H":', len(h))
print ('Всего слов на "I":', len(i))
print ('Всего слов на "J":', len(j))
print ('Всего слов на "K":', len(k))
print ('Всего слов на "L":', len(l))
print ('Всего слов на "M":', len(m))
print ('Всего слов на "N":', len(n))
print ('Всего слов на "O":', len(o))
print ('Всего слов на "P":', len(p))
print ('Всего слов на "Q":', len(q))
print ('Всего слов на "R":', len(r))
print ('Всего слов на "S":', len(s))
print ('Всего слов на "T":', len(t))
print ('Всего слов на "U":', len(u))
print ('Всего слов на "V":', len(v))
print ('Всего слов на "W":', len(w))
print ('Всего слов на "X":', len(x))
print ('Всего слов на "y":', len(y))
print ('Всего слов на "Z":', len(z))

dots = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for x, y, d in zip(X, Y, dots):
    plt.scatter(x, y, s=35)
    plt.text(x-0.43, y-0.43, d)


plt.bar(X, Y, color='orchid')
plt.show()

