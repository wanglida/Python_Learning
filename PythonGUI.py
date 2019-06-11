# 本代码初步学习PythonGUI编程

import tkinter as tk # 导入 tk inter

class App:
    def __init__(self, root):
        # 添加一个label
        label1=tk.Label(root, text='Hello Tkinter')  # label的文字为Hello Tkinter
        label1.pack()  # 把label标签放在主窗口上
        # button
        # button属性包括：activebackground,activeforebackground,bd,bg,conmmand执行函数,fg字颜色,font,height,
        # highlightcolor高亮颜色,image,justify（多行文本对齐方式，LEFT\RIGHT\CENTER）,padx,pady(X和Y轴的内边距)
        # ，relief（边框样式，FLAT\SUNKEN\RAISED\GROOVE\RIDGE）,state（按钮组件状态，NORMAL\ACTIVE\DISABLED）
        # ,underline,width,wraplength,text,anchor_
        button1 = tk.Button(root,
                                 text='Button1',
                                 bg='blue',
                                 fg='orange',
                                 height=3,
                                 width=20)
        button1.pack(side=tk.LEFT)  # 将button1放在窗口上的左侧
        button2 = tk.Button(root,
                                 text='按钮2',
                                 bg='green',
                                 fg='grey',
                                 activebackground='red')
        button2.pack(side=tk.RIGHT)  # 将button2放在窗口上的右侧
        button3 = tk.Button(root,
                                 text='调用函数',
                                 fg='purple',
                                 command=self.buttoncall)
        # command是控件加载时的事件处理函数，调用buttoncall函数，在控制台观察调用结果
        button3.pack()

    def buttoncall(self):
        # 设计一个函数，用来调用button
        print("Python command", "调用成功。")


root = tk.Tk()
app = App(root)
root.mainloop()  # 保持主窗口运行


