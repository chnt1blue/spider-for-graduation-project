'''
获取新网页
获取网页的指定内容,有一些简单的分词我也写在里面了
陈瑜
'''
from bs4 import BeautifulSoup
import word_cut
import sys
sys.setrecursionlimit(1000000) #例如这里设置为一百万
import global_list
class HtmlParser(object):
    def __init__(self):
        self.jieba =  word_cut.Jieba()
    def parse(self, url, content, html_encode="utf-8"):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, "html.parser", \
            from_encoding=html_encode)
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        new_url = "https://www.proginn.com/wo/" + str(global_list.GLOBAL_B)
        global_list.GLOBAL_B = global_list.GLOBAL_B + 1
        new_urls.add(new_url)
        return new_urls

    """
    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/href/\w+"))
        print (links)
        for link in links:
            url_path = link["href"]
            print (url_path)
            new_url = urljoin(url, url_path)
            new_urls.add(new_url)
        return new_urls
"""

    def _get_new_data(self, url, soup):
        # 1网址
        data = {"url": url}
        # 2昵称
        nn_node = soup.find("div", class_="nickname")
        data["nickname"] = nn_node.get_text()
        # 3工作地点,工作单位
        i_node = soup.find("div", class_="introduction")
        if i_node:
            try:
              result1 = i_node.get_text()
              result2 = i_node.get_text().split()
              data["location"] = result2[0]
              data["company"] = result1[len(result2[0]) + 1:]
            except Exception as e:
              data["location"] = ''
              data["company"] = ''
        # 4工作简讯
        hi_node = soup.find("div", class_="hire-info")
        if hi_node is None:
            data["work-price"]=""
            data["work-location"] = ""
            data["work-mode"] = ""
            data["work-time"] = ""
        else:
            result4 = hi_node.get_text().split()
            data["work-price"] = result4[0]
            #下面的工作时间和工作地点是通过判断来获得的,如果时间地点间没有东西了,就证明
            #该用户没写,下同
            location_num = result4.index('可工作地点:')
            time_num = result4.index('可工作时间:')
            max_len = len(result4)
            difference1 = time_num - location_num
            difference2 = max_len - 1 - time_num
            if difference1 == 1:
                data["work-location"] = ""
                data["work-mode"] = ""
            else:
                data["work-location"] = result4[location_num + 1]
                data["work-mode"] = result4[location_num + 2]
            if difference2 == 1:
                data["work-time"] = ""
            else:
                data["work-time"] = result4[time_num + 1]
        # 5履历
        p_node = soup.find("div", class_="panel")
        if p_node is None:
            data["panel"]=""
            data["panel2"] = ""
        else:
            data["panel"] = p_node.get_text()
            data["panel2"] = self.jieba.change_data(data["panel"])
        # 6工作经历/教育经历
        jp_node = soup.find_all("div", class_="history-list")
        if jp_node is None:
          data["J_Experiences-list"] = ""
        elif len(jp_node)==0:
           data["J_Experiences-list"] = ""
        else:
           data["J_Experiences-list"] = jp_node
        # 7技能表
        sk_node = soup.find_all("div", class_="name")
        if sk_node is None:
            data["skill-list"]=""
        elif len(sk_node)==0:
           data["skill-list"] = ""
        else:
            data["skill-list"] = sk_node
        # 8作品
        works_node = soup.find("div", class_="works")
        if works_node is None:
            data["works"]=""
        else:
            data["works"] = works_node.get_text()
        #9评价
        pj_node = soup.find("div", class_="ui comments")
        if pj_node is None:
            data["ui comments"] = ""
        else:
            data["ui comments"] = pj_node.get_text()
        print (data)
        return data
