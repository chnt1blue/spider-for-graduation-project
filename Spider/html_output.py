"""
目前暂时以网页形式输出,便于观察和改动,后期差不多了存进数据库里
陈瑜
"""
import time
import global_list
class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_name = time.strftime("%Y-%m-%d")
        with open("%s-%s-%s.html" % (file_name , global_list.GLOBAL_A , global_list.GLOBAL_A+global_list.GLOBAL_C), "w", encoding='utf-8') as f_out:
            f_out.write("<html>")
            f_out.write(r'<head>'
                        r'<link rel="stylesheet" '
                        r'href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" '
                        r'integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" '
                        r'crossorigin="anonymous"></head>')
            f_out.write("<body>")
            f_out.write(r'<table class="table table-bordered table-hover">')
            item_css = ['active', 'success', 'warning', 'info']
            f_out.write('<td>网址</td>' )
            f_out.write('<td>昵称</td>')
            f_out.write('<td>所在地点</td>')
            f_out.write('<td>公司/前公司</td>' )
            f_out.write('<td>日薪</td>' )
            f_out.write('<td>工作方式</td>')
            f_out.write('<td>可工作地点</td>' )
            f_out.write('<td>工作时间</td>' )
            f_out.write('<td width="2000">个人介绍</td>' )
            f_out.write('<td width="2000">个人介绍_分词后</td>')
            f_out.write('<td width="2000">工作经历/教育经历</td>' )
            f_out.write('<td>掌握的技能</td>')
            f_out.write('<td>作品</td>' )
            f_out.write('<td>评价</td>')
            for data in self.datas:
                index = self.datas.index(data) % len(item_css)
                f_out.write(r'<tr class="'+item_css[index]+r'">')
                f_out.write('<td>%s</td>' % data["url"])
                f_out.write('<td>%s</td>' % data["nickname"])
                f_out.write('<td>%s</td>' % data["location"])
                f_out.write('<td>%s</td>' % data["company"])
                f_out.write('<td>%s</td>' % data["work-price"])
                f_out.write('<td>%s</td>' % data["work-location"])
                f_out.write('<td>%s</td>' % data["work-mode"])
                f_out.write('<td>%s</td>' % data["work-time"])
                f_out.write('<td width="2000">%s</td>' % data["panel"])
                f_out.write('<td width="2000">%s</td>' % data["panel2"])
                f_out.write('<td>%s</td>' % data["J_Experiences-list"])
                f_out.write('<td>%s</td>' % data["skill-list"])
                f_out.write('<td>%s</td>' % data["works"])
                f_out.write('<td>%s</td>' % data["ui comments"])
                f_out.write("</tr>")

            f_out.write("</table>")
            f_out.write("</body>")
            f_out.write("</html>")