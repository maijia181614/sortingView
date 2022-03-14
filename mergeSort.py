import copy
from data import dataClass

def mergeSort(data_set):
    frames = [data_set]#获取原始数据
    ds = copy.deepcopy(data_set)
    splitMerge(ds, 0, dataClass.dataCount, frames)
    frames.append(ds)
    return frames

def splitMerge(ds, head, tail, frames):#归并
    mid = (head + tail) // 2#计算中间节点
    if tail - head > 2:#分开左右两块再次递归归并,直到不能再分
        splitMerge(ds, head, mid, frames)
        splitMerge(ds, mid, tail, frames)
    ds_yb = copy.deepcopy(ds)
    left = head#左边分区的头
    right = mid#右边分区的头
    tmp_list = []
    for i in range(head, tail):#排序合并过程
        frames.append(copy.deepcopy(ds_yb))#加入一份数据
        if right == tail or (left < mid and ds[left].value <= ds[right].value):#左右区间每一个数据进行比较，从小到大加入列表
            tmp_list.append(ds[left])
            frames[-1][left].setColor('#ff00ff')#加入的数据设置颜色提醒
            left += 1#比较完移动
        else:
            tmp_list.append(ds[right])
            frames[-1][right].setColor('#ff00ff')#加入的数据设置颜色提醒
            right += 1#比较完移动
    for i in range(head, tail):
        ds[i] = tmp_list[i-head]#取出临时链表中的值
    frames.append(copy.deepcopy(ds))