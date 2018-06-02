# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 17:12
# @Author  : SHeynckes
# @Email   : shenghai@ymail.com
# @File    : FileSearcher.py
# @Software: PyCharm

# 本程序利用GUI开发一个跨平台的文件搜索软件
# 根据关键字在一个文件夹中搜索某种格式（扩展名）的文件
# 双击搜索出的文件名后，自动打开该文件

from tkinter import *
import os
from tkinter import filedialog, messagebox, scrolledtext


def func():
    str1 = ent1.get()
    str2 = ent2.get()
    if not (str1 and str2):
        messagebox.showinfo("Warning", "Please input the keywords and file type first!")
        return
    folder = filedialog.askdirectory()
    if not folder:
        return

    listbox.delete(0, END)

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.split(".")[-1] == str2:
                with open(root + "/" + file) as f:
                    if str1 in f.read():
                        listbox.insert(END, root + "/" + file)


def open_file(arg):
    if not listbox.curselection():
        return
    window = Tk()
    path = listbox.get(listbox.curselection(), last=None)
    file_name = path.split("/")[-1]
    window.title(file_name)
    text = scrolledtext.ScrolledText(window, width=100)
    text.grid()
    with open(path) as f:
        text.insert(END, f.read())


root = Tk()
# 修改窗口的名字
root.title("File Searcher")
# 修改窗口的位置
root.geometry("+700+300")

Label(root, text="Keywords: ").grid(row=0, column=0)
ent1 = Entry(root)
ent1.grid(row=0, column=1)
Label(root, text="File Type: ").grid(row=0, column=2)
ent2 = Entry(root)
ent2.grid(row=0, column=3)
btn = Button(root, text="Choose Folder", command=func)
btn.grid(row=0, column=4)

var1 = StringVar()
listbox = Listbox(root, width=80, listvariable=var1)
listbox.bind("<Double-Button-1>", open_file)
listbox.grid(row=1, column=0, columnspan=5)

root.mainloop()
