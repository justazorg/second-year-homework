import urllib.request
import re
import os
t = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
with urllib.request.urlopen(t) as a:
    html = a.read().decode('utf-8')
   
slova_na_c = re.findall(r'\bс\w+\b', html)
print('\n'.join(slova_na_c))
print('Всего слов на <<с>>:', len(slova_na_c))
no_repeat_c = []
for line in slova_na_c:
    if line not in no_repeat_c:
        no_repeat_c.append(line)
print('\n'.join(no_repeat_c))
print('Всего слов на <<с>> без повторений:', len(no_repeat_c))

