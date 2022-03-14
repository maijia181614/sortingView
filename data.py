import math

class dataClass:#数据类 存放值与颜色值，方便处理
    dataCount=40

    def __init__(self,value):
        self.value = value
        self.setColor()

    def setColor(self,rgba = None):#根据数据值大小范围设置渐变颜色值
        if not rgba:
            if(self.value<self.dataCount/3):
                r=255
                g=math.ceil(255*3*self.value/self.dataCount)
                b=0
            elif(self.value<self.dataCount/2):
                r=math.ceil(750-self.value*(250*6/self.dataCount))
                g=255
                b=0
            elif(self.value<self.dataCount*2/3):
                r=0
                g=255
                b=math.ceil(self.value*(250*6/self.dataCount)-750)
            elif(self.value<self.dataCount*5/6):
                r=0
                g=math.ceil(1250-self.value*(250*6)/self.dataCount)
                b=255
            else:
                r=math.ceil(150*self.value*(6/self.dataCount)-750)
                g=0
                b=255
            rgba=(r/256,g/256,b/256,1)


        self.color=rgba