#输入输出
#str=input("请输入：")
#print("输入的内容是：",str)

#打开和关闭文件
fp=open("TestFile.txt","r+")
print("文件名：",fp.name)
print("关闭状态：",fp.closed)
print("访问模式：",fp.mode)

text=fp.read()
print("读取的字符串为：",text)  #读取尽可能多的字符并输出
position=fp.tell()
print("当前文件位置：",position)  #查找当前文件指针位置
position=fp.seek(0,0)  #把指针重新定位到文件开头
text=fp.read(6)
print("重新读取：",text)
fp.close()
print("执行close()后，关闭状态：",fp.closed)