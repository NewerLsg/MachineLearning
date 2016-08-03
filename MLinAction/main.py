import kNN
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

'''
group,label=kNN.createDataset()
pos=array([0.5,0.5])
count=kNNClassify.classify0(pos,group,label,2)
print count 
'''

def main(datingDataMat,datinglabels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datinglabels),15.0*array(datinglabels))
    plt.show()


def datingSetTest(horate):
	datingDataMat,datingLabel=kNN.file2matrix('datingTestSet2.txt')		
        print "data[%d]:%s,\nlabel:%s" %(datingDataMat.shape[0],datingDataMat,datingLabel)
	datingDataMat,rangeval,minval=kNN.autonorm(datingDataMat)
        print "data[%d]:%s" %(datingDataMat.shape[0],datingDataMat)
	m=datingDataMat.shape[0]
	count=int(m*horate)
        errcount=0.0
        for i in range(1,count):
            retVal=kNN.classify0(datingDataMat[i,:],datingDataMat[count:m,:],datingLabel[count:m],3)
            print "orignal:%d,calculate:%d"%(datingLabel[i],retVal)
            if retVal != datingLabel[i]:
				errcount+=1.0
				print "error."
        print "error rate:%f" %(errcount/float(count))

def classifyPerson():
    resultlist=['not at all','in small doss','in large does']
    percentTats=float(raw_input("percentage of time spent playing video game?"))
    ffMiles=float(raw_input("frequent filer miles earned per year?"))
    icecream=float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabel = kNN.file2matrix('datingTestSet2.txt')
    normat,rangeval,minval=kNN.autonorm(datingDataMat)
    print "normat:%s" %(normat)
    inX=array([ffMiles,percentTats,icecream]) 
    retVal=kNN.classify0((inX - minval)/rangeval,normat,datingLabel,3)
    print "retval[%d]" %(retVal)
    print "resutl:%s " %(resultlist[retVal])

def classifyImg(trainingdir,testdir):
    trainingfiles=listdir(trainingdir)
    filecount=len(trainingfiles)
    print "trainingfiles:%d" %(filecount)
    trainMatrixData=zeros((filecount,1024))
    label = []
    index = 0
    for i in range(filecount):
        fields = trainingfiles[i].split('_');
        num = fields[0]
        label.append(num)
        filepath=trainingdir + '/' + trainingfiles[i]
        trainMatrixData[index,:] = kNN.img2matrix(filepath)
    testfiles=listdir(testdir)    
    filecount =  len(testfiles)/10
    errcount = 0.0
    print "testfiles:%d" %(filecount)
    for i in range(filecount):
        fields = testfiles[i].split('_');
        num = fields[0]
        filepath=testdir + '/' + testfiles[i]
        testMatrix = kNN.img2matrix(filepath)
        retval = kNN.classify0(testMatrix, trainMatrixData,label,3)
        print "ret val:%d,real:%d" %(int(retval),int(num))
        if (int(retval) != num):
            errcount += 1
            print "error"
    print "rate:%f"%(errcount/float(filecount))

print "start..."
classifyImg('trainingDigits','testDigits')

print "end."

