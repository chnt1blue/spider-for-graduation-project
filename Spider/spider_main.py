from Spider import url_manager, html_downloader, html_parser, html_output,word_cut
import global_list
'''
爬虫主程序,设定爬虫头,爬取数量和起始网页
陈瑜
'''
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.out_put = html_output.HtmlOutput()
        self.jieba = word_cut.Jieba()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/"
                                  "537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
                }
                html_content = self.downloader.download(new_url, retry_count=2, headers=headers)
                new_urls, new_data = self.parser.parse(new_url, html_content, "utf-8")
                self.urls.add_new_urls(new_urls)
                self.out_put.collect_data(new_data)
                if count >= global_list.GLOBAL_C:#设置爬取数量
                    break
                count = count + 1
            except Exception as e:
                print("craw failed!\n"+str(e))
        self.out_put.output_html()


if __name__ == "__main__":
    rootUrl = "https://www.proginn.com/wo/"+str(global_list.GLOBAL_A)
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)
