from selenium import webdriver

class ChromeDriver():
    #### constructor ####
    def __init__(self):
        # 옵션 생성
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument("headless")
        # # 드라이버 실행
        self.__driver = webdriver.Chrome(options=self.__options)
        self.__cUrl = ""

    def driverOn(self):
        """
        크롬 드라이버 실행
        :param cUrl: 크롬드라이버로 실행할 초기 주소
        """
        self.__driver.get(self.__cUrl)

    def driverOff(self):
        """
        크롬드라이버 종료
        """
        self.__driver.quit()

    def buttonClick(self, id):
        """
        페이지 버튼을 눌러 페이지를 이동하는 함수
        :param id: 버튼의 XPath
        """
        self.__driver.find_element_by_xpath(f"{id}").click();

    def googleSendKeys(self, searchKeys):
        element = self.__driver.find_element_by_name('q')
        element.send_keys(searchKeys)
        element.submit()

    def naverSendKeys(self, searchKeys):
        element = self.__driver.find_element_by_name('query')
        element.send_keys(searchKeys)
        element.submit()

    ####__getter__####
    # __url
    def __getUrl__(self):
        """
        현재 크롬드라이버가 탐색중인 페이지의 url을 리턴하는 함수
        :return: 현재 페이지의 주소(String)
        """
        return self.__driver.current_url

    #### __setter__ ####
    def setUrl(self, cUrl):
        self.__cUrl = cUrl