from bs4 import BeautifulSoup
import global_list
class HtmlParser(object):
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
        new_url = "https://www.proginn.com/wo/" + str(global_list.GLOBAL_A)
        global_list.GLOBAL_A = global_list.GLOBAL_A + 1
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
        if nn_node is None:
            data["nickname"]=""
        else:
            data["nickname"] = nn_node.get_text()
        # 3简介
        i_node = soup.find("div", class_="introduction")
        if i_node is None:
             data["introduction"] = ""
        else:
            data["introduction"] = i_node.get_text()
        # 4工作简讯
        hi_node = soup.find("div", class_="hire-info")
        if hi_node is None:
            data["hire-info"]=""
        else:
            data["hire-info"] = hi_node.get_text()
        # 5履历
        p_node = soup.find("div", class_="panel")
        if p_node is None:
            data["panel"]=""
        else:
            data["panel"] = p_node.get_text()
        # 6工作经历
        jp_node = soup.find("div", class_="panel proginn-work-history")
        if jp_node is None:
            data["J_Experiences-list"] = ""
        else:
            data["J_Experiences-list"] = jp_node.get_text()
        # 7技能表
        sk_node = soup.find("div", class_="skill-list")
        if sk_node is None:
            data["skill-list"]=""
        else:
            data["skill-list"] = sk_node.get_text()
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
        return data
