from ChromeDriverController import ChromeDriver
from GoogleCrawler import GoogleCrawler
from NaverCrawler import NaverCrawler

def OverlapCheck(list1, list2):
    """
    중복검사 함수
    검색결과 중 url이 중복될 경우 같은 검색결과로 보고 하나만 검색 결과에 넣음
    :param list1: google 검색 결과 리스트
    :param list2: naver 검색 결과 리스트
    :return resultList: 중복을 제거하고 두 리스트를 합친 리스트
    """
    resultList = list2
    for l1 in list1:
        i = 0
        for l2 in list2:
            if l1[2] == l2[2]:
                print("중복발생")
                i = 1
        if i == 0:
            resultList.append(l1)
    return resultList

def PriorityCheck(rList, sContent):
    resultList = []
    """
    우선순위 결정 리스트
    질의와 검색결과의 일치하는 글자수로 점수를 책정
    :param rList: 중복이 제거된 검색결과 리스트
    :param sContent: 검색에 사용된 질의
    :return: 우선순위 점수가 추가된 검색결과 리스트
    """
    for l in rList:
        score = 0
        for c in sContent:
            if c in l[1]:
                if c != " ":
                    score += 1
        l[3] = score
        resultList.append(l)
    return resultList

def SearchEngineScore(rList):
    """
    각 검색엔진의 우선순위 점수 평균을 계산하는 함수
    :param rList: 중복이 제거되고 우선순위 점수가 추가된 검색결과 리스트
    :return:
    """
    googleScore = 0
    naverScore = 0
    cnt = 0
    for i in rList:
        if i[0] == "Google":
            googleScore += i[3]
            cnt += 1
        else:
            naverScore += i[3]
    googleScore = googleScore/cnt
    naverScore = naverScore / (len(rList) - cnt)
    return googleScore, naverScore

if __name__ == "__main__":
    # 검색할 질의
    searchContent = input("질의 입력 : ")
    # 크롬 드라이버 객체 생성
    cd = ChromeDriver()
    # google 크롤러 객체 생성
    gc = GoogleCrawler()
    # naver 크롤러 객체 생성
    nc = NaverCrawler()

    # google 검색
    cd.setUrl('https://www.google.com/')
    cd.driverOn()
    cd.googleSendKeys(searchContent)
    gc.crawl(cd.__getUrl__())
    googleResult, googleResultURL = gc.getResult()

    # google 검색결과 리스트
    googleSearchList = []
    for j, k in zip(googleResult, googleResultURL):
        googleSearchList.append(["Google", j, k, 0])

    # naver 검색
    cd.setUrl('https://www.naver.com/')
    cd.driverOn()
    cd.naverSendKeys(searchContent)
    nc.crawl(cd.__getUrl__())
    naverResult, naverResultURL = nc.getResult()

    # naver 검색결과 리스트
    naverSearchList = []
    for j, k in zip(naverResult, naverResultURL):
        naverSearchList.append(["Naver", j, k, 0])

    # 크롬 드라이버 종료
    cd.driverOff()

    checkedList = OverlapCheck(googleSearchList, naverSearchList)

    resultList = PriorityCheck(checkedList, searchContent)

    resultList.sort(key=lambda x:-x[3])

    for i in resultList:
        print(i)

    googleScore, naverScore = SearchEngineScore(resultList)

    print("검색 결과")

    print(f"____________________Google____________________")
    for i in googleSearchList:
        print(i)
    print(f"______________________________________________")

    print(f"____________________Naver____________________")
    for i in naverSearchList:
        print(i)
    print(f"_____________________________________________")

    print("총 결과")
    for i in resultList:
        print(i)

    print(f"구글 검색 결과 수 : {len(googleSearchList)}")
    print(f"구글 검색 정확도 : {googleScore}")

    print(f"네이버 검색 결과 수 : {len(naverSearchList)}")
    print(f"네이버 검색 정확도 : {naverScore}")
