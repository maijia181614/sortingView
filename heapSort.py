import copy
from data import dataClass

doneCount = 0
haveDone = [doneCount]#存放每一步已排序的数据个数

def heapSort(data_set):
    global doneCount
    global haveDone
    frames = [data_set]#获取原始数据

    ds = copy.deepcopy(data_set)
    for i in range(dataClass.dataCount//2-1, -1, -1):#从最后一个父节点构建最大堆，不断调整
        heapAdjust(ds, i, dataClass.dataCount, frames)
    for i in range(dataClass.dataCount-1, 0, -1):
        ds[i], ds[0] = ds[0], ds[i]#不断取出大堆顶，交换到已排序的数列的尾部
        doneCount = doneCount + 1#更新已排序的数据个数
        heapAdjust(ds, 0, i, frames)#取出堆顶之后重新调整最大堆
    frames.append(ds)#加入最后的数据
    haveDone.append(doneCount)
    return frames,haveDone

def heapAdjust(ds, head, tail, frames):#调整堆
    global doneCount
    global haveDone
    i = head * 2 + 1#父节点的左孩子
    while i < tail:
        if i + 1 < tail and ds[i].value < ds[i+1].value:#如果还没到尾节点，则先选择其中值较大的一个孩子节点
            i += 1
        ds_c = copy.deepcopy(ds)
        frames.append(ds_c)#加入一份上一步处理完成的数据
        haveDone.append(doneCount)
        ds_c[i].setColor('r')#要比较的孩子节点与父节点颜色提醒
        ds_c[head].setColor('black')
        if ds[i].value <= ds[head].value:#若较大的都比父节点小，不调整堆
            break
        ds[head], ds[i] = ds[i], ds[head]#否则将较大的孩子节点与父节点交换
        ds_c = copy.deepcopy(ds_c)
        frames.append(ds_c)#加入一份设置完提醒父节点与孩子节点的数据
        haveDone.append(doneCount)
        ds_c[head], ds_c[i] = ds_c[i], ds_c[head]
        head = i#移动父节点与孩子节点，继续调整
        i = i * 2 + 1