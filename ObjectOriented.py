class Fruit:
    #水果类
    weight=0
    price=0
   
    def __init__(self,name,weight,price):  # 以下是构造函数
        self.name=name
        self.weight=weight
        self.price=price
    
    def displayPrice(self):
        print("%d元/千克"%self.price)
    
    def displayWeight(self):
        print("%d千克"%self.weight)


apple=Fruit("hongfushi",1,18)  # 创建一个对象，代表红富士苹果，1单位重量，18单位价格
print("这只",apple.name,"的价格为",apple.price,"元/千克")  # 对象调用属性
print(apple.name," ")
apple.displayPrice()  # 计算并输出该苹果的价格
