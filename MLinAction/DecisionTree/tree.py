from math import log

def  caculateShang(dataSet):
    count=len(dataSet)
    statisticsSet = {} 
    for row in dataSet:
        kind = row[-1]
        if kind not in statisticsSet.keys():
            statisticsSet[kind] = 0
        statisticsSet[kind] += 1
    retval = 0.0
    for key in statisticsSet.keys():
        pro=statisticsSet[key]/float(count)
        retval -= pro * log(pro,2)
    return retval

def createDataSet():
    dataSet = [[1,1,'yes'],
            [1,1,'yes'],
            [1,0,'no'],
            [0,1,'no'],
            [0,1,'no']]
    label = ['no surfacing','flippers']
    return dataSet,label

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for item in dataSet:
        if item[axis] == value:
            featItem=item[:axis]
            featItem.extend(item[axis+1:])
            retDataSet.append(featItem)
    return retDataSet

def choseBestFeature(dataSet):
    amount=len(dataSet)
    features=len(dataSet[0]) - 1
    print "amount:%d,features:%d"%(amount,features)
    bestShang=caculateShang(dataSet)
    bestInfoGain = 0.0
    beatfeature = features
    for i in range(features):
        featValList=[example[i] for example in dataSet]
        uniqueValList=set(featValList)
        print "uinquevalist:%s"%(uniqueValList)
        newshang = 0.0
        for j in uniqueValList:
            subDataSet=splitDataSet(dataSet,i,j)
            weight= len(subDataSet)/float(amount)
            newshang += weight * caculateShang(subDataSet)
        infoGain = bestShang - newshang
        print "bestShang:%s newshang:%s"%(bestShang,newshang)
        if infoGain > 0:
            bestInfoGain = infoGain
            bestShang = newshang
            beatfeature = i
    return beatfeature

def majorcnt(classify):
    classifyCount = {}
    for i in classify: 
        if i not in classifyCount.keys():
            classifyCount[i] = 0
        classifyCount[i] += 1
    sortedClassifyCount = sort(classifyCount.iteritems(),key=operator.itemgetter(1),reverse=True) 
    return sortedClassifyCount[0][0]

def tree(dataSet,label):
    classify=[example[-1] for example in dataSet]
    print "classify:%s" %(classify)
    if classify.count(classify[0]) == len(classify):
        return classify[0]
    if len(dataSet[0]) == 1:
        return majorcnt(classify)
    bestFeature=choseBestFeature(dataSet)
    bestFeatureLabel=label[bestFeature]
    print "bestFeature:%s,conent[%s]" %(bestFeature, label[bestFeature])
    myTree={bestFeatureLabel:{}}
    del(label[bestFeature])
    featureList=[example[bestFeature] for example in dataSet]
    uniqueFeatureList=set(featureList)
    for i in uniqueFeatureList:
        subLabel=label[:]
        myTree[bestFeatureLabel][i]=tree(splitDataSet(dataSet,bestFeature,i),subLabel)
    return myTree
