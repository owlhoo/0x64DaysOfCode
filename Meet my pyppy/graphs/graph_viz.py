import pygraphviz as pvg

G = pvg.AGraph("firstone.dot")
G.draw('test.svg', format='svg', prog='dot')