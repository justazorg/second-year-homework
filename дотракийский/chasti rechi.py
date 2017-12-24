import re
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


def open_html(f):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
content = open_html(r'C:\Users\muhni\Desktop\дотракийский\словарик.html')
v = re.findall(r'''v\.''', content)
adj = re.findall(r'''adj\.''', content)
adv = re.findall(r'''adv\.''', content)
conj = re.findall(r'''conj\.''', content)
det = re.findall(r'''det\.''', content)
n = re.findall(r'''n\.''', content)
intj = re.findall(r'''intj\.''', content)
na = re.findall(r'''na\.''', content)
ni = re.findall(r'''ni\.''', content)
np = re.findall(r'''np\.''', content)
num = re.findall(r'''num\.''', content)
pn = re.findall(r'''pn\.''', content)
prep = re.findall(r'''prep\.''', content)
prop = re.findall(r'''prop\.''', content)
vin = re.findall(r'''vin\.''', content)
vtr = re.findall(r'''vtr\.''', content)
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Y = [len(v), len(adj), len(adv), len(conj), len(det), len(n), len(intj), len(na), len(ni), len(np), len(num), len(pn), len(prep), len(prop), len(vin), len(vtr)]

dots = ['v', "adj", "adv", "conj", "det", "n", "intj", "na", "ni", "np", "num", "pn", "prep", "prop", "vin", "vtr"]

for x, y, d in zip(X, Y, dots):
    plt.scatter(x, y, s=35)
    plt.text(x-0.43, y-0.43, d)


plt.bar(X, Y, color='orchid')
plt.show()

