import pydotplus
graph_a = pydotplus.graph_from_dot_file('firstone.dot')     # read from dot file
graph_a.write_svg('test.svg')                               # generates svg graph
