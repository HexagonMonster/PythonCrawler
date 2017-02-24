# coding:utf8

import re

from bs4 import BeautifulSoup

from baike_crawler.py_version import py_version

if py_version == 3:
    from urllib import parse as urlparse
else:
    import urlparse


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        # new_urls = set()
        new_urls = []
        # /view/123.htm /subview/123.htm
        links = soup.find_all('a', href=re.compile(r'/(sub)?view(/\d+)+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_full_url = self._simplify_url(new_full_url)
            # new_urls.add(new_full_url)
            if new_full_url not in new_urls:
                new_urls.append(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summay_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summay_node.get_text()

        return res_data

    def _simplify_url(self, url):
        simp_url = url
        hash_index = simp_url.find('#')
        if hash_index != -1:
            simp_url = simp_url[:hash_index]

        question_index = simp_url.find('?')
        if question_index != -1:
            simp_url = simp_url[:question_index]

        if simp_url != url:
            print('-- simplified: {} -> {}'.format(url, simp_url))
        return simp_url
