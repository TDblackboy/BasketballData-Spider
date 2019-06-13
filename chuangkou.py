# 用于展示数据

import json
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
'''
窗口展示
'''

# 设计分析如何展示
# button添加事件

# 窗体类
class Window:

    # 初始化window将root赋给self（对象变量）
    def __init__(self,root,data):
        self.root=root
        self.data = data
        self.init_window()

    def init_window(self):
        self.root.title("Mango")
        self.root.geometry("400x300")
        b1 = tk.Button(self.root, text='首发数据分析结果', width=15, height=2,command=self.bangding1)
        b1.pack()
        b2 = tk.Button(self.root, text='篮板数据分析结果', width=15, height=2,command=self.bangding2)
        b2.pack()
        b3 = tk.Button(self.root, text='助攻数据分析结果', width=15, height=2,command=self.bangding3)
        b3.pack()
        b4 = tk.Button(self.root, text='上场数据分析结果', width=15, height=2,command=self.bangding4)
        b4.pack()
        b5 = tk.Button(self.root, text='得分数据分析结果', width=15, height=2,command=self.bangding5)
        b5.pack()

    # button绑定事件 - 图形化展示
    def bangding1(self):
        #加载数据
        datas=self.data
        shoufa_data=datas["shoufa"]
        #print(type(shoufa_data))
        #print(type(shoufa_data[0]))
        shoufa_data = list(map(int, shoufa_data))#将list中每一个str->int
        shoufa_data.sort()
        num=len(shoufa_data)
        #创建图形
        labels=players
        name_list = labels
        num_list = shoufa_data
        plt.xlabel('name')
        plt.ylabel('First episode')
        plt.title('Toronto Raptors(TOR)')
        plt.bar(range(len(num_list)),num_list,tick_label=name_list)
        plt.show()

    def bangding2(self):
        #加载数据
        datas=self.data
        lanban_data=datas["lanban"]
        #print(type(shoufa_data))
        #print(type(shoufa_data[0]))
        lanban_data = list(map(str, lanban_data))#将list中每一个str->int
        lanban_data.sort()
        #创建图形
        x = players
        y = lanban_data
        plt.xlabel('name')
        plt.ylabel('Backboard')
        plt.title('Toronto Raptors(TOR)')
        plt.scatter(x, y, c='r', marker='o')  # c = 'r'表示散点的颜色为红色，marker 表示指定三点多形状为圆形
        plt.show()

    def bangding3(self):
        # 加载数据
        datas = self.data
        data = datas["zhugong"]
        data = list(map(str, data))  # 将list中每一个str->int
        data.sort()
        # 创建图形
        x = players
        y = data
        plt.plot(x, y, linewidth=5)
        # 设置标题及坐标轴标签，并设置字体大小
        plt.title("Toronto Raptors(TOR)", fontsize=20)
        plt.xlabel("Name", fontsize=14)
        plt.ylabel("Assists", fontsize=14)
        # 设置刻度尺
        plt.tick_params(axis='both', labelsize=14)
        plt.show()

    def bangding4(self):
        # 加载数据
        datas = self.data
        data = datas["shangchang"]
        data = list(map(str, data))  # 将list中每一个str->int
        data.sort()
        # 创建图形
        labelss = players
        num_list = data
        plt.title('Toronto Raptors(TOR):Point guard')
        plt.pie(x=num_list, labels=labelss)
        plt.show()

    def bangding5(self):
        #加载数据
        datas=self.data
        defen_data=datas["defen"]
        #print(type(shoufa_data))
        #print(type(shoufa_data[0]))
        defen_data = list(map(str, defen_data))#将list中每一个str->int
        defen_data.sort()
        #创建图形
        labelss=players
        num_list = defen_data
        plt.title('Toronto Raptors(TOR):Point guard')
        plt.pie(x=num_list,labels=labelss)
        plt.show()


# 对外调用的生成窗体的方法
def chuang(data):
    root = tk.Tk()
    win = Window(root,data)
    root.mainloop()

# util-读取json数据
def readJson(path):
    with open(path, 'r', encoding='utf-8') as json_file:
        reading = json.load(json_file)# 存放读取的数据
    # print(reading)
    # print(type(reading))
    reading=eval(reading)
    # print(type(reading))
    #shoufa_data = reading["shoufa"]
    #print(type(shoufa_data))
    #print(shoufa_data)
    #lenss = len(shoufa_data)
    #print(lenss)
    return reading


# 球员名
players=["Leonard","Siakam","Ibaka","Lowry","Jonas",
         "Fred","Green","Marc","Powell","OG",
         "Jeremy","Delon","Jodie","Miles","Greg",
         "Miller","Chris","Patrick","Loyd","Brown",
         "Eric","Malachi"]
# 主函数
if __name__ == '__main__':
    print("test start.....")
    path=u"D:\\篮球数据爬取\\parser_data.json"
    data=readJson(path)
    chuang(data)
    print("test end.......")