import tkinter
root=tkinter.Tk()
#label
label1=tkinter.Label(root, text='Hello Tkinter')
label1.pack()  #把label标签放在主窗口上

def buttoncall():
    print("Python command","调用成功。")


#button
#button属性包括：activebackground,activeforebackground,bd,bg,conmmand执行函数,fg字颜色,font,height,highlightcolor高亮颜色,image
#,justify（多行文本对齐方式，LEFT\RIGHT\CENTER）,padx,pady(X和Y轴的内边距)
#，relief（边框样式，FLAT\SUNKEN\RAISED\GROOVE\RIDGE）,state（按钮组件状态，NORMAL\ACTIVE\DISABLED）
#,underline,width,wraplength,text,anchor_
button1=tkinter.Button(root,
                       text='Button1',
                       bg='blue',
                       fg='orange',
                       height=3,
                       width=20)
button1.pack(side=tkinter.LEFT)
button2=tkinter.Button(root,
                       text='按钮2',
                       bg='green',
                       fg='grey',
                       activebackground='red')
button2.pack(side=tkinter.RIGHT)

button3=tkinter.Button(root,
                       text='调用函数',
                       fg='purple',
                       command=buttoncall())  #command是控件加载时的事件处理函数
button3.pack()

root.mainloop()  ##保持主窗口运行
