import graphviz  # doctest: +NO_EXE
"""Generate a pdf file of a graph viz diagram from python code."""
dot = graphviz.Digraph(comment='The Round Table')
#dot  #doctest: +ELLIPSIS
#<graphviz.graphs.Digraph object at 0x... >

dot.node('A', 'King Arthur')  # doctest: +NO_EXE
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)  # doctest: +NORMALIZE_WHITESPACE +NO_EXE
#// The Round Table
#digraph {
#    A [label="King Arthur"]
#    B [label="Sir Bedevere the Wise"]
#    L [label="Sir Lancelot the Brave"]
#    A -> B
#    A -> L
#    B -> L [constraint=false]
#}
#doctest_mark_exe()

dot.render('round-table.gv').replace('\\', '/')
#'doctest-output/round-table.gv.pdf'
