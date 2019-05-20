#列表练习
listM=['math','physics','chemistry','biology']
listC=['Chinese','English','politics','history']
listG=['Geography']

print(listM[2])
print("Subjects : ",listM+listC+listG)  #+号表示列表的连接
listM.append('Information Technology')  #列表最后添加一个元素
print(listM*2)  #重复输出列表二次
del listC[3]
print(listC)  #删除列表第4元素
listC.append(['World history','Chinese history'])  #列表之后又新加了一个列表作为原列表的元素
print(listC)
print(max(listM))  #列表listM的最大值
print(len(listM))  #列表listM的长度
print(listM.count('math'))  #统计列表中math元素出现的个数
listM.reverse()  #反转元素的位置
print(listM,"\n")


#元组
zoo=('wolf','tiger','elephant')
print('The number of zoos ',len(zoo),'The second is :', zoo[1])
#元组不能修改，但能连接组合
zoo_new=('lion','bear','raccon','kangroo','fox')
whole_zoo=zoo+zoo_new
print('The whole zoo includes:',whole_zoo)
#字典
dict={'a':12,'b':18,'c':16}
print("\nb:",dict['b'])
dict['b']=23  #更新字典
dict['d']=19  #添加数据
del dict['a']  #删除键是a的条目
##dict.clear() 清空字典
##del dict  删除字典
print('字典:',dict,'\n字典大小：',len(dict))
