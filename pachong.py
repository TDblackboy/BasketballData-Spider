# 爬取 - 分析 - 保存 数据

import os
import urllib.request
from bs4 import BeautifulSoup;
import json

'''
篮球数据分析
'''

# Util - 存储爬取到的html
def saveHTML(save_path, filename, content):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"\\"+filename+".txt"
    with open(path, "w+",encoding='utf-8') as fp:
        fp.write(content)
    print("saved.........")

# Util - 存储解析到的JSON
def saveParserData(save_path, filename, parserData):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"\\"+filename+".json"
    #print(parserData)
    jsonData=json.dumps(parserData) # 字典转为json
    print(jsonData)
    with open(path, "w",encoding='utf-8') as file:
        json.dump(jsonData, file)
    print("加载入JSON文件完成...")

# Util- 分析数据-找到有用的数据
def extract(html):
    soup = BeautifulSoup(html,'html.parser')
    trs=soup.find_all('tr',class_='sort')
    #print(trs)
    parserData={}
    shoufas=[]
    lanbans = []
    zhugongs = []
    shangchangs = []
    defens = []
    for tr in trs:
        # 首发次数
        shoufa=tr.findAll('td')[3]
        shoufas.append(shoufa.getText())
        #print(shoufa)
        # 篮板次数
        lanban = tr.findAll('td')[14]
        lanbans.append(lanban.getText())
        # 助攻次数
        zhugong = tr.findAll('td')[17]
        zhugongs.append(zhugong.getText())
        # 上场时间
        shangchang = tr.findAll('td')[4]
        shangchangs.append(shangchang.getText())
        # 得分
        defen = tr.findAll('td')[22]
        defens.append(defen.getText())
    # print(shoufas)
    # print(shangchangs)
    # print(lanbans)
    # print(zhugongs)
    # print(defens)
    parserData["shoufa"]=shoufas
    parserData["shangchang"]=shangchangs
    parserData["lanban"]=lanbans
    parserData["zhugong"]=zhugongs
    parserData["defen"]=defens
    #print(parserData)
    return parserData

# 对外调用的接口爬虫
def Spider(url):
    print("downloading......... ", url)
    page = urllib.request.urlopen(url).read() .decode("utf-8")
    parserData=extract(page)
    save_path = u"D:\\篮球数据爬取"
    filename = u"parser_data"
    saveParserData(save_path,filename,parserData)

# 执行程序 main方法入口
if __name__ == '__main__':
    print("Spider start.....")
    target_url = "http://www.stat-nba.com/team/TOR.html"
    Spider(target_url)
    print("Spider end.....")