import kNN
import kNNClassify
from numpy import *
import operator

group,label=kNN.createDataset()
pos=array([0.5,0.5])
count=kNNClassify.classify0(pos,group,label,2)
print count 
