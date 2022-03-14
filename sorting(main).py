import random
import matplotlib
matplotlib.use('TKAgg')
from matplotlib import pyplot as plt#引入绘图相关函数
from matplotlib import animation#引入绘制动图的函数
from data import dataClass#数据类
from bubbleSort import bubbleSort#引入排序算法
from heapSort import heapSort
from mergeSort import mergeSort
import tkinter
plt.rcParams['font.family'] = ['Heiti TC']#设置支持中文字体  mac:font.family Heiti TC  windows:font.sans-serif SimHei




def createDataSource():#生成排序用的原始数据
    data = []
    data = list(range(1, dataClass.dataCount+1))
    random.shuffle(data)#打乱生成的数据
    return data



def drawChart(originalData,intervals,sortNumber):#画出图表
    xlabel=['冒泡排序可视化','堆排序可视化','归并排序可视化']#标题列表
    axsTitle=['bubbleSorting','HeapSorting','mergeSorting']#标题列表
    sortList = [bubbleSort, heapSort, mergeSort]#排序算法列表
    fig = plt.figure('B类17排序可视化测试', figsize=(10, 6), facecolor='#888888')#创建基础面板
    data_set=[dataClass(d) for d in originalData]#初始化数据
    axs = fig.add_subplot(111)#添加子图
    axs.set_xticks([])#设置坐标轴
    axs.set_yticks([])#设置坐标轴
    axs.set_xlabel(xlabel[sortNumber])#设置坐标轴
    plt.subplots_adjust(left=0.01, bottom=0.2, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)#子图位置调整
    if(sortNumber!=2):#选择展示的排序算法,传入原始数据，经过算法处理后返回所有帧数的原始数据
        ProcessdData, haveDone = sortList[sortNumber](data_set)
    else:
        ProcessdData=sortList[sortNumber](data_set)

    def animate(fi):#更新图画的函数
        bars=[]#条形图集
        if(len(ProcessdData)>fi):#fi为当前帧数，只要还未达到整个动画的最终帧数，就一直更新
            axs.cla()#清除画板,以下重新设置子图上的条形图
            axs.set_title(axsTitle[sortNumber],color='w',fontsize='large')#设置标题
            axs.set_xticks([])#坐标轴同上
            axs.set_yticks([])
            axs.set_xlabel(xlabel[sortNumber],color='w',fontsize='large')
            if (sortNumber != 2):#显示某些算法中已排序的数据个数和步数
                plt.text(0, dataClass.dataCount, '已排序：'+ str(haveDone[fi]))
            plt.text(0, dataClass.dataCount-2,  '步数：' + str(fi))
            bars += axs.bar(list(range(dataClass.dataCount)),  # 条形图设置 x轴范围
                            [d.value for d in ProcessdData[fi]],  # 取出每次排序的全部数据  就是高度
                            1,  # 宽度
                            color=[d.color for d in ProcessdData[fi]],# 设置颜色
                            alpha=0.7
                            ).get_children()#条形图合集
        return bars

    anim=animation.FuncAnimation(fig,animate,frames=len(ProcessdData),interval=intervals)#动态生成
    return plt,anim



if __name__ == "__main__":

    dataClass.dataCount=40#设置原始数据的个数
    originalData = createDataSource()#创建要排序的原始数据
    interval=60#刷新频率
    root = tkinter.Tk()#以下是开始的窗体设置
    root.title("请选择")
    root.geometry('230x45')
    def on_click(sN):
        global sortN
        sortN=sN
        global root
        root.destroy()
    button1 = tkinter.Button(root, text='冒泡排序', font=('Arial', 12), width=7, height=1, command=lambda: on_click(0))
    button2 = tkinter.Button(root, text='堆排序', font=('Arial', 12), width=7, height=1, command=lambda: on_click(1))
    button3 = tkinter.Button(root, text='归并排序', font=('Arial', 12), width=7, height=1, command=lambda: on_click(2))
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    root.mainloop()
    plt, _ = drawChart(originalData, interval, sortN)  # 根据选择画出图形
    plt.show()#展示