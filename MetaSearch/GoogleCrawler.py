from bs4 import BeautifulSoup as bs
import requests

class GoogleCrawler:
    #### constructor ####
    def __init__(self, __searchResult = None, __searchResultURL = None):
        self.__searchResult = __searchResult or []
        self.__searchResultURL = __searchResult or []

    #### function ####
    def crawl(self, url):
        """
        주어진 페이지의 정보를 파싱하는 함수
        :param url: ChromeDriver 가 탐색중인 페이지의 url 으로 bs4로 파싱할 목표 주소
        """
        self.url = url
        resp = requests.get(self.url)
        soup = bs(resp.text, 'lxml')
        searchResult = []
        searchResultURL = []
        for i in range(len(soup.select('.BNeawe.vvjwJb.AP7Wnd'))):
            searchResult.append(soup.select('.BNeawe.vvjwJb.AP7Wnd')[i].text)
            searchResultURL.append(soup.select('.kCrYT > a')[i]['href'][7:])
        self.setResult(searchResult, searchResultURL)


    #### __getter__ ####
    def getResult(self):
        return self.__searchResult, self.__searchResultURL

    #### __setter__ ####
    def setResult(self, searchResult, searchResultURL):
        self.__searchResult = searchResult
        self.__searchResultURL = searchResultURL
