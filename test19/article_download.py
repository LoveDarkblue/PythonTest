# 1.url,content
# 2.截取文章内容
# 3.写到文件
import requests
import sys
from bs4 import BeautifulSoup


class article_download():
    def __init__(self, url, target, filename):
        self.server = url
        self.target = url + target
        self.filename = filename
        self.titles = []
        self.urls = []
        self.nums = 0

    def initData(self):
        re = requests.get(self.target)
        soup = BeautifulSoup(re.text, 'lxml')
        # print(soup.title)
        all_div = soup.find_all('div', class_='listmain')
        # print(all_div[0])
        all_a = BeautifulSoup(str(all_div[0]), 'lxml').find_all('a')
        self.nums = len(all_a[15:30]) - 1
        for info in all_a[15:30]:
            self.titles.append(info.string)
            self.urls.append(self.server + info.get('href'))

    def getContent(self, contentUrl):
        recontent = requests.get(contentUrl)
        all_content = BeautifulSoup(recontent.text, 'lxml').find_all('div', class_='showtxt')
        return all_content[0].text.replace('\xa0' * 8, '\n\n')

    def writefile(self, content):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(content)
            file.write('\n\n')

    def start11(self):
        if len(self.titles) <= 0:
            print('no titles')
            return
        print('%s 开始下载' % self.filename)
        for (i, title), url in zip(enumerate(self.titles), self.urls):
            # print(i, title, url)
            self.writefile(title + '\n' + self.getContent(url))
            sys.stdout.write("  已下载:%.3f%%" % (float(str(i)) / self.nums) + '\r')
            sys.stdout.flush()
        print('%s 下载完成' % self.filename)


if __name__ == "__main__":
    download = article_download('http://www.biqukan.com/', '1_1094', "一年永恒.txt")
    download.initData()
    # download.getContent('http://www.biqukan.com/1_1094/17747241.html')
    download.start11()
