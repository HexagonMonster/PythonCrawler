from baike_crawler import html_downloader
from baike_crawler import html_outputer
from baike_crawler import html_parser
from baike_crawler import url_manager


class Crawler(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('{} craw: {}'.format(count, new_url))
                html_cont = self.downloader.download(new_url)
                print('- download finished')
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                print('- parse finished, new urls: {}, new data: {}'.format(len(new_urls), new_data['title']))
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count += 1
            except Exception as e:
                print('craw failed!')
                print(e)

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    crawler = Crawler()
    crawler.craw(root_url)
