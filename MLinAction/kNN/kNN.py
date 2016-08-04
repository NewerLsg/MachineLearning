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
        classLabelVector.append(int(fileds[-1].strip()))
        index += 1 
    return returnMat,classLabelVector 

def autonorm(dataSet):
   maxval = dataSet.min(0)
   minval = dataSet.max(0)
   rangeval = maxval - minval
   normalSet=zeros(shape(dataSet))
   m=dataSet.shape[0]
   normalSet=dataSet-tile(minval, (m, 1))
   normalSet=normalSet/tile(rangeval, (m, 1))
   return normalSet,rangeval,minval

def img2matrix(filename):
    fr=open(filename)
    matrixDat=zeros((1,1024))
    for i in range(32):
        line=fr.readline()
        for j in range(32):
           matrixDat[0,i*32+j] = line[j]
    return matrixDat
