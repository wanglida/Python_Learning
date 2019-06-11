try:
    fp=open("testfile","w")
    fp.write("This is a new test file for exception.")
except IOError:
    print("Error:没有找到文件或读取文件失败！")
else:
    print("内容写入成功！")
    fp.close()
