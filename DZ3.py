import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import sys
import gensim, logging
import networkx as nx
import  matplotlib.pyplot as plt



m = 'C:\\Users\\muhni\\Desktop\\prjct\\ruscorpora_upos_skipgram_300_5_2018.vec.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.KeyedVectors.load(m)

words = ['картошка_NOUN', 'баклажан_NOUN', 'огурец_NOUN', 'яблоко_NOUN', 'тыква_NOUN']

n = model.similarity('картошка_NOUN', 'баклажан_NOUN')
n1 = model.similarity('картошка_NOUN', 'огурец_NOUN')
n2 = model.similarity('картошка_NOUN', 'яблоко_NOUN')
n3 = model.similarity('картошка_NOUN', 'тыква_NOUN')
n4 = model.similarity('баклажан_NOUN', 'огурец_NOUN')
n5 = model.similarity('баклажан_NOUN', 'яблоко_NOUN')
n6 = model.similarity('баклажан_NOUN', 'тыква_NOUN')
n7 = model.similarity('яблоко_NOUN', 'огурец_NOUN')
n8 = model.similarity('огурец_NOUN','тыква_NOUN')
n9 = model.similarity('яблоко_NOUN','тыква_NOUN')
print(n, n1, n2, n3, n4, n5, n6, n7, n8, n9)

G = nx.Graph()
G.add_nodes_from(['картошка_NOUN', 'баклажан_NOUN', 'огурец_NOUN', 'яблоко_NOUN', 'тыква_NOUN'])
G.add_edges_from([('картошка_NOUN', 'баклажан_NOUN'),('картошка_NOUN', 'огурец_NOUN'), ('картошка_NOUN', 'тыква_NOUN'), ('баклажан_NOUN', 'огурец_NOUN'), ('баклажан_NOUN', 'тыква_NOUN'), ('яблоко_NOUN', 'огурец_NOUN'), ('огурец_NOUN', 'тыква_NOUN')])
print('узлы', G.nodes())
print('рёбра', G.edges())

pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='pink', node_size=120)
nx.draw_networkx_edges(G, pos, edge_color='orange')
plt.axis('on')
plt.show()

print(nx.radius(G))

deg = nx.degree_centrality(G)
for nodeid in sorted(deg, key=deg.get, reverse=True):
    print('Центральные узлы:',nodeid)

print(nx.average_clustering(G))
print(nx.transitivity(G))








      
