from numpy import *

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split() #strip 剥离空格
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn,classLabels):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m,n = shape(dataMatrix) #m特征个数 n数据点个数
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1)) #特征系数初始值为1
    for k in range(maxCycles):
        # dataMatrix*weights 特征与特征系数 矩阵相乘的结果 放入sigmoid函数中 得出h
        # h为n*1维列向量 保存临时01分类结果 返回和真实值相同类型的label值0,1
        h = sigmoid(dataMatrix*weights) 
        # 计算真实类别与预测类别的差值
        error = (labelMat - h)
        # 按照差值的方向调整回归系数
        weights = weights + alpha * dataMatrix.transpose() * error
        #print(k)
    
    # 返回回归系数
    return weights

def plotBestFit(wei):
    import matplotlib.pyplot as plt
    
    weights = wei.getA() # 转成数组
    dataMat,labelMat = loadDataSet() # 数组形式返回
    dataArr = array(dataMat) #?
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x = arange(-3.0,3.0,0.1) #-3到3,间隔0.1
    # y ?
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('X1');plt.ylabel('X2')
    plt.show()