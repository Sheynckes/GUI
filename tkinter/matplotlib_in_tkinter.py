# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 17:44
# @Author  : SHeynckes
# @Email   : shenghai@ymail.com
# @File    : matplotlib_in_tkinter.py
# @Software: PyCharm

# 在数据分析的过程中，往往需要对所建立的模型进行可视化，并调整其中的某些参数。
# 通常情况下，在Python中可以通过Matplotlib来进行绘制图像。
# 然而该绘制过程是静态的，也就是每次调整完参数后，都需要重新调用绘图语句进行绘图展示。
# 本程序的目标是结合GUI组件，实现对模型参数的交互式绘图（散点图）。
# 这样，可以在展示出的GUI界面中动态地调整模型参数，并绘制图像。

import numpy as np
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class Application(tk.Tk):
    """
    文件夹选择程序，界面与逻辑分离
    """
    def __init__(self):
        """
        初始化
        """
        super(Application, self).__init__()
        self.wm_title("Embed Matplotlib in tkinter")

        fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()

        # 放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
        foot_frame = tk.Frame(master=self)
        foot_frame.pack(side=tk.BOTTOM)
        tk.Label(master=foot_frame, text="Sample Number: ").pack(side=tk.LEFT)
        self.input_entry = tk.Entry(master=foot_frame)
        self.input_entry.pack(side=tk.LEFT)
        self.input_entry.insert(0, "50")
        tk.Button(master=foot_frame, text="Plot", command=self.draw).pack(side=tk.LEFT)

        self.draw()

    def draw(self):
        """
        绘图逻辑
        :return:
        """
        # 获取GUI界面中需要设置的参数
        try:
            sample_count = int(self.input_entry.get())
        except:
            sample_count = 50
            # print("Please input an integer: ")
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, "50")

        x = np.random.randint(0, 100, size=sample_count)
        y = np.random.randint(0, 100, size=sample_count)

        self.ax.clear()
        self.ax.scatter(x, y, s=3)
        self.canvas.show()

    def _quit(self):
        """
        退出
        :return:
        """
        self.quit()
        self.destroy()


if __name__ == "__main__":
    # 实例化Application
    app = Application()
    # 主消息循环
    app.mainloop()
