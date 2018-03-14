'''
分词,用的是python jieba
目前还很简单
'''
import jieba
from jieba import analyse
class Jieba(object):

  def change_data(self,data):
        #jieba.analyse.textrank("", topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
        tfidf = analyse.extract_tags
        #jieba.load_userdict("dict.txt")
        cut1 = jieba.cut_for_search(data)
        cut2 = tfidf(data, topK=40, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
        s = ('/'.join(cut1))
        return cut2
