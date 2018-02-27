class UrlManager(object):

    """new_urls表示新的未爬取的路径，一旦其被选择爬去就变成old_urls，这就意味着所有的路径只分为new和old这两种"""
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        """被选择出来的路径需要立即添加到old_urs里面去"""
        self.old_urls.add(new_url)
        return new_url