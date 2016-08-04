from numpy import *
import operator
def classify0(inX, dataSet, label, k):
    print "inX:%s\ndataSet:%s\nlabel:%s\nk:%d\n" %(inX,dataSet,label,k)
    dataSetSize = dataSet.shape[0]
    print "size:%d" %(dataSetSize)
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    print "diffMat:%s\n" %(diffMat)   
    sqDiffMat = diffMat**2
    print "sqDiffMat:%s\n" %(sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances**0.5
    print "distance:%s\n" %(distance) 
    sortDisIndicies = distance.argsort()
    print "sortDisIndicies:%s" %(sortDisIndicies)
    classCount={}
    for i in range(k):
        voteIlabel=label[sortDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount=sorted(classCount.iteritems(),
    key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
