# coding:utf8


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w', encoding='utf-8') as fout:

            fout.write('<html>\n')
            fout.write('<meta charset=\'utf-8\'>\n')
            fout.write('<body>\n')
            fout.write('<table>\n')

            for data in self.datas:
                fout.write('<tr>\n')
                fout.write('<td>{}</td>\n'.format(data['url']))
                fout.write('<td>{}</td>\n'.format(data['title']))
                fout.write('<td>{}</td>\n'.format(data['summary']))
                fout.write('</tr>\n')

            fout.write('</table>\n')
            fout.write('</body>\n')
            fout.write('</html>\n')
