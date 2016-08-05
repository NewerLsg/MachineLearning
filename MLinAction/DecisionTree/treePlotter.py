import matplotlib.pyplot as plt
decisionNode=dict(boxstyle='sawtooth',fc="0.8")
leafNode=dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")

def plotNode2(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt, xycoords='axes fraction', xytext= centerPt, textcoords='axes fraction', va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xytext=centerPt,bbox=nodeType,arrowprops=arrow_args)

def createPlot2():
    fig=plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('a decision node', (0.5,0.1), (0.1,0.5), decisionNode)
    plotNode('a leaf node', (0.8,0.1), (0.3,0.8), leafNode)
    plt.show()

def getLeafNum(treeData):
    leafnum = 0
    firstKey=treeData.keys()[0]
    secondKey=treeData[firstKey]
    for keyItem in secondKey.keys():
        if type(secondKey[keyItem]).__name__ == 'dict':
            leafnum += getLeafNum(secondKey[keyItem]) 
        else:
            leafnum += 1
    return leafnum

def getTreeDept(treeData):
    firstKey=treeData.keys()[0]
    secondKey=treeData[firstKey]
    maxDept=0
    for keyItem in secondKey.keys():
        if type(secondKey[keyItem]).__name__ == 'dict':
            dept = 1 + getTreeDept(secondKey[keyItem])
            if dept > maxDept:
                maxDept = dept
        else:
            maxDept=1
    return maxDept

def retrieveTree(i):
    listOfTree=[{'no surfacing':{0:'no',1:{'flippers':\
                {0:'no',1:'yes'}}}},
            {'no surfacing':{0:'no',1:{'flippers':\
                {0:{'head':{0:'no',1:'yes'}},1:'no'}}}}
            ]
    return listOfTree[i]

def plotMidTxt(cntNode, parentNode,txt):
    midx = (parentNode[0] - cntNode[0])/2 + cntNode[0]
    midy = (parentNode[1] - cntNode[1])/2 + cntNode[1]
    createPlot.ax1.text(midx,midy,txt)

def plotTree(myTree, parentNode, nodeTxt):
    numLeaf=getLeafNum(myTree)
    dept=getTreeDept(myTree)
    firstStr=myTree.keys()[0]
    cntNode=(plotTree.xOff + (1.0 + float(numLeaf))/2.0/plotTree.totalW,plotTree.yOff)
    plotMidTxt(cntNode,parentNode,nodeTxt)
    plotNode(firstStr,cntNode,parentNode,decisionNode)
    secondKey=myTree[firstStr]
    plotTree.yOff=plotTree.yOff - 1.0/plotTree.totalD
    for key in secondKey.keys():
        if type(secondKey[key]).__name__ == 'dict':
            plotTree(secondKey[key],cntNode,str(key))
        else:
            plotTree.xOff=plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondKey[key],(plotTree.xOff,plotTree.yOff),cntNode,leafNode)
            plotMidTxt((plotTree.xOff, plotTree.yOff),cntNode,str(key))
    plotTree.yOff = plotTree.yOff + 1/plotTree.totalD

def createPlot(inTree):
    fig=plt.figure(1, facecolor='white')
    fig.clf()
    axprops=dict(xtrix=[],yticks=[])
    createPlot.ax1=plt.subplot(111,frameon=False)
    plotTree.totalW=float(getLeafNum(inTree))
    plotTree.totalD=float(getTreeDept(inTree))+1
    plotTree.xOff= -0.5/plotTree.totalW;plotTree.yOff=1
    plotTree(inTree,(0.5,1.0),'')
    plt.show()

def classify(inTree, label, testVec):
    firstStr=inTree.keys()[0] 
    vecIndex=label.index(firstStr)
    secondKey=inTree[firstStr]
    for key in secondKey.keys():
        if testVec[vecIndex] == key:
            if type(secondKey[key]).__name__ == 'dict':
                classlabel = classify(secondKey[key], label, testVec)
            else:
                classlabel = secondKey[key]
    return classlabel
