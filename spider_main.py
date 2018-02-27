import url_manager, html_downloader, html_parser, html_outputer
"""URL管理器   HTML下载器   HTML解析器   HTML输出器"""


class SpiderMain(object):
    def __init__(self):
        """绑定属性的方法，第一参数永远是self，表示创建的类实例本身感觉相当于this"""
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        """爬虫入口函数"""
        count = 1
        self.urls.add_new_url(root_url)
        """添加根路径到new_urls中"""
        while self.urls.has_new_url():
            """有新的URL"""
            """因为页面中有些页面的URL可能已经失效了所以我们爬取页面的时候需要加入异常处理"""
            try:
                new_url = self.urls.get_new_url()
                """获取现在要爬去的URL"""
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break
                count = count+1
            except:
                print('Craw failed!')

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)