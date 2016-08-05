import tree
import treePlotter
fr=open('lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLable=['age','prescript','astigmatic','tearRate']
print lensesLable

lensesTree=tree.tree(lenses,lensesLable)
treePlotter.createPlot(lensesTree)
print lensesTree
