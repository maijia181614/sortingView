import copy
from data import dataClass


def bubbleSort(dataSet):
    frames = [dataSet]#获取原始数据
    doneCount=0
    haveDone=[doneCount]#存放每一步骤已排序的个数
    tempDataSet = copy.deepcopy(dataSet)
    for i in range(dataClass.dataCount-1):#外层循环这么多次
        flag = False
        for j in range(dataClass.dataCount-i-1):#内层循环次数
            if tempDataSet[j].value>tempDataSet[j+1].value:#左边的大就交换
                tempDataSet[j], tempDataSet[j+1]= tempDataSet[j+1],tempDataSet[j]
                flag = True
            frames.append(copy.deepcopy(tempDataSet))#加入一次排序的数据
            frames[-1][j+1].setColor('#ff00ff')#选中排序的变红
            haveDone.append(doneCount)#加入已排序的个数
        if not flag:
            doneCount = doneCount + 1
            break


        doneCount=doneCount+1

    doneCount = dataClass.dataCount
    frames.append(tempDataSet)
    haveDone.append(doneCount)

    return frames,haveDone