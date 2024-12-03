from typing import List
import os
import requests
from bs4 import BeautifulSoup



URL = "https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%B9%B4%E5%8F%B7%E5%88%97%E8%A1%A8/14920380"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

def getHTML(url):
    try:
        with open('html.txt','w',encoding='utf-8') as f:
            f.write(requests.get(url, headers=HEADERS).text)
        print("html write OK")
    except:
        print("html get went wrong")


def parse() :
    """
    使用BeautifulSoup提取帖子标题、作者、发布日期，基于css选择器提取
    需要注意的时，我们在提取帖子的时候，可能有些帖子状态不正常，会导致没有link之类的数据，所以我们在取值时最好判断一下元素长度
    :param html_content: html源代码内容
    :return:
    """
    with open('dict.txt','w', encoding='utf-8') as f:
        soup = BeautifulSoup(open('html.txt', encoding='utf-8'), "lxml")
    
        divs=soup.find_all('div',attrs={'data-tag': 'module'})
        for ex,div in enumerate(divs):
            ths=div.find_all('th')
            Emperor=0
            year=0
            for i,th in enumerate(ths):
                span = th.find('span')
                if span.text == '年号':
                    Emperor = i
                elif span.text == '起讫时间':
                    year = i
            
            trs=div.find_all('tr')
            jump=0
            ee_to_write:str='-'
            yy_to_write:str='-'
            for tr in trs:
                tds=tr.find_all('td')
                if len(tds) ==1:
                    continue;
                for i,td in enumerate(tds):
                    if jump>0:
                        e=Emperor-1
                        y=year-1
                    else:
                        e=Emperor
                        y=year
                    if i == e :
                        ee_to_write=td.text
                        
                    elif i == y:
                        yy_to_write=td.text
                        
                if yy_to_write !='-':
                    f.write(ee_to_write+':'+yy_to_write+'\n')
                # 确保 tds 列表不为空
                if len(tds) > 0 and jump<=0:
                    # 安全地获取 rowspan 属性，使用 get 防止 KeyError
                    rowspan = tds[0].get('rowspan')
                    
                    if rowspan:  # 如果有 rowspan 属性
                        jump = int(rowspan)
                jump-=1

    print("读入完成")

if __name__ == '__main__':
    if not os.path.exists('html.txt'):
        getHTML(URL)
        
    parse()