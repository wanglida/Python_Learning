class Fruit:
    '水果类'
    weight=0
    price=0
    # 以下是构造函数
    def __init__(self,name,weight,price):
        self.name=name
        self.weight=weight
        self.price=price
    def displayPrice(self):
        print("%d元/千克"%self.price)
    def displayWeight(self):
        print("%d千克"%self.weight)

apple=Fruit("hongfushi",1,18)
print("这只",apple.name,"的价格为",apple.price,"元/千克")
print(apple.name," ")
apple.displayPrice()
