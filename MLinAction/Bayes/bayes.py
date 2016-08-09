from numpy import *

def loadDataSet():
    docList = [['my','dog','has','flea','problems','please'],\
            ['maybe','not','take','him','to','dog','park','stupid'],\
            ['my','dalmation','is','so','cute','r','love','him'],\
            ['stop','posting','stupid','worthless','garbage'],\
            ['mr','licks','ate','my','steak','how','to','stop','him'],\
            ['quit','buying','worthless','dog','food','stupid']]
    
    classVec = [0,1,0,1,0,1]
    return docList,classVec

def createVocabList(dataSet):
    vocabList = set([])
    for item in dataSet:
        vocabList = vocabList | set(item)
    return list(vocabList)

def word2set(inputTxt,vocabList):
    returnVec = [0] * len(vocabList)
    for word in inputTxt:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
        else:
            print "%s not in vocablist." %(word)
    return returnVec

def trainNB0(doclist,vocabList,classVec):
    docnum=len(classVec)
    pVec1=sum(classVec)/float(len(classVec))
    pvocab0 = ones(len(vocabList)); pvocab1 = ones(len(vocabList))
    pc0=2.0; pc1=2.0 
    for i in range(docnum):
        wordSet = word2set(doclist[i],vocabList)
        if classVec[i] == 1:
            pvocab1 += wordSet
            pc1 += sum(wordSet)
        else:
            pvocab0 += wordSet
            pc0 += sum(wordSet)
    pvocab0 = log(pvocab0/pc0)
    pvocab1 = log(pvocab1/pc1)
    return pvocab0,pvocab1,pVec1

def classifyNB(vec2classify, p0Vec, p1Vec, pc1):
    p0= sum(vec2classify * p0Vec) + log(pc1)
    p1= sum(vec2classify * p1Vec) + log(1 - pc1)
    if p0 > p1:
        return 0
    else:
        return 1

def testClassifyNB():
    data, label = loadDataSet()
    vocabList = createVocabList(data)
    pv0, pv1, pc1 = trainNB0(data,vocabList,label)
    testEntry=['love','my','dalmation'] 
    thisDoc=array(word2set(testEntry,vocabList))
    print  testEntry,'classified as:', classifyNB(thisDoc,pv0,pv1,pc1)
    testEntry=['stupid','garbage'] 
    thisDoc=array(word2set(testEntry,vocabList))
    print  testEntry,'classified as:', classifyNB(thisDoc,pv0,pv1,pc1)

def textPrase(bigString):
    import re
    words=re.split(r'\W*',bigString)
    return [tok.lower() for tok in words if len(tok) > 2]

def verifyNB():
    doclist=[];label=[]
    for i in range(1,26):
        wordlist=textPrase(open('./email/spam/%d.txt'%i).read())
        doclist.append(wordlist)
        label.append(1)
        wordlist=textPrase(open('./email/ham/%d.txt'%i).read())
        doclist.append(wordlist)
        label.append(0)
    vocabList=createVocabList(doclist)
    trainSet=range(50);testSet=[]
    for i in range(10):
        randindex = int(random.uniform(0,len(trainSet)))
        testSet.append(trainSet[randindex]) 
        del(trainSet[randindex])
    trainDocList=[];testDocList=[]
    trainLabel=[]
    for i in trainSet:
        trainDocList.append(doclist[i])
        trainLabel.append(label[i])
    p0list,p1list,pc1=trainNB0(array(trainDocList),vocabList,array(trainLabel))
    errCount = 0.0
    for i in testSet:
        vablist=array(word2set(doclist[i], vocabList))
        ret = classifyNB(vablist,p0list,p1list,pc1)
        print ret
        if ret != label[i]:
            print 'err:ret %d label[%d] %d\n'%(ret,i,label[i]),
            errCount += 1 
    
    print errCount

print 'testing'
verifyNB()
print 'ended.'

