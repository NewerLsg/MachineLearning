from numpy import *
import operator

def createDataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]) 
    labels = ['A','A','B','B']
    return group,labels 

def classify0(inX, dataSet, label, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances**0.5
    sortDisIndicies = distance.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=label[sortDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount=sorted(classCount.iteritems(),
    key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr=open(filename)
    lines=fr.readlines()
    linecount=len(lines)
    returnMat=zeros((linecount,3))
    classLabelVector=[]
    index=0
    for line in lines:
        fileds=line.split('\t')
        returnMat[index,:]=fileds[0:3]
        classLabelVector.append(int(fileds[-1]))
        index += 1
    return returnMat,classLabelVector
