print('Hello world! What\'s your name?')  #Hello World
print("双引号引用中文.What's up?")  #中文
print('''这是三引号下的字符串
可以作为段落，\
引用多行''')  #行末的\表示字符串在下一行继续，而不是开始一个新行
print(u"This is a Unicode字符串")
a=11;b=2;c=a*b;d=a**b  #乘方
print(c,d)  #不换行输出
print("2左移8",(2<<8))
a=31415.e-8  #科学计数法表示小数
print('科学计数法',a)
#控制流 if语句
num=3
if num<5:
    print("该数小于5：num=",num)
elif num==5:
    print("该数等于5，num=",num)
else:
    print("概述大于5：num=",num)
#while循环
res=0
while res<9:
    print('The result is :',res)
    res+=1
#for 循环
for letter in "IamIronMan":
    print("当前字母：",letter)
AllFruits=['苹果','香蕉','桃子','葡萄','others']
for fruit in AllFruits:
    print('当前水果:',fruit)
#定义函数
def sayHello(a,b,c="末尾"):  #只有在形参表末尾的那些参数可以有默认参数值
    global x
    x=6
    print('Hello! The fuction!a=',a,'b=',b,'c=',c)
    print('函数内x=',x)
#调用函数
x=8
sayHello(3,4)
print('x=',x)

#文档字符串 Doc Strings
#Filename func_docp.py
def printMax(xx,yy):
    '''prints the max number of two numbers.
    The two values must be integers.'''
    x=int(xx);y=int(yy)
    if xx>yy:
        print(xx,"is max")
    else :
        print(yy,"is max")
printMax(6,8)
print(printMax.__doc__)

