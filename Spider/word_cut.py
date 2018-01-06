import jieba
class Jieba(object):

  def change_data(self,data):
       s = data
       s = jieba.cut(s,cut_all= 1)
       return s