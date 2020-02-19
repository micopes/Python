# 파도 정보 분석

학과 | 학번 | 성명
---- | ---- | ---- 
정보컴퓨터공학부 |201524404 |강민진


## 프로젝트 개요
기상청에서 공공데이터를 검색해서 풍속, 풍향, 파고, 파주기, 파향 에 대한 정보를 받았다.
https://data.kma.go.kr/data/sea/selectBuoyRltmList.do?pgmNo=52
좋은 파도의 요건을 함수로 만들었다. (countFunc)
좋은 파도인지 구별하는 조건은 2개로 둘다 만족하는 것을 찾고자 하였다.
풍속, 풍향, 파고, 파주기, 파향 각각 점수를 매겨 80점이 넘으면 count를 1점씩 올리도록 만들었다.
(countFunc)
4점이상의 count를 받은 파도를 좋은 파도로 평가할 수 있게 만들었다.
또한, 5분야의 점수를 모두 합쳐 550점을 넘는 것을 좋은 파도로 평가하도록 만들었다.
(scoreFunc)
엑셀파일을 입력받아 판다스를 이용해서 형식에 맞게 나눠주었다.
리스트를 이용해서 각 분야를 함수에 대입하여 원하는 점수, count를 얻었다.
그래프를 이용해서 나타내었다.
그래프 이외에도 리스트를 이용해서 조건을 만족시키는 값을 출력할 수 있도록 만들었고, 과거의 값 뿐만아니라 미래의 날씨도 적절하게 대입하여 날씨 정보를 파악할 수 있게 만들었다.


## 사용한 공공데이터 
[데이터보기](https://github.com/cybermin/python2019/blob/master/%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%EC%97%AD%EC%82%AC%EC%A0%95%EB%B3%B4_20190520.csv)
https://data.kma.go.kr/data/sea/selectBuoyRltmList.do?pgmNo=52

## 소스
* [링크로 소스 내용 보기](https://github.com/cybermin/python2019/blob/master/tes.py) 

* 코드 삽입

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def scoreFunc(windspeed, winddirection, waveheight, waveperiod, wavedirection) :

    a = (33 - windspeed) * 5 # 풍속
    if winddirection > 180 :
        b = 120 - abs(360 - winddirection) # 풍향
    else :
        b = 120 - abs(winddirection - 0)
    if a > 120 :
        b = b + 50
    elif a > 100 :
        b = b + 25
    c = waveheight * 150 # 파고
    d = waveperiod  * 15
    e = 130 - abs(180 - wavedirection)

    return a + b + c + d + e

def countFunc(windspeed, winddirection, waveheight, waveperiod, wavedirection) :
    global count
    count = 0
    a = (33 - windspeed) * 5 # 풍속
    if winddirection > 180 :
        b = 120 - abs(360 - winddirection) # 풍향
    else :
        b = 120 - abs(winddirection - 0)
    if a > 120 :
        b = b + 50
    elif a > 100 :
        b = b + 25
    c = waveheight * 150 # 파고
    d = waveperiod  * 15
    e = 130 - abs(180 - wavedirection)
    if a > 80 :
        count = count + 1
    if b > 80 :
        count = count + 1
    if c > 80 :
        count = count + 1
    if d > 80 :
        count = count + 1
    if e > 80 :
        count = count + 1

    return count

df = pd.read_csv('2018다대포2.csv', encoding = 'cp949') #쉼표사이에 파일경로/파일명.csv
df.columns = ['위치', 'date', '풍속', '풍향', '파고', '파주기', '파향']
del df['위치']

windspeed = df.groupby(df.date.str[:10]).mean()['풍속'] # 뒤에 [index]붙여서 각각 표현 가능 0부터 시작.
winddirection = df.groupby(df.date.str[:10]).mean()['풍향']
waveheight = df.groupby(df.date.str[:10]).mean()['파고']
waveperiod = df.groupby(df.date.str[:10]).mean()['파주기']
wavedirection = df.groupby(df.date.str[:10]).mean()['파향']

scoreList = []
countList = []

for i in range(0, 91) :
    scoreList.append(int(scoreFunc(windspeed[i], winddirection[i], waveheight[i], waveperiod[i], wavedirection[i])))
    countList.append(countFunc(windspeed[i], winddirection[i], waveheight[i], waveperiod[i], wavedirection[i]))

scoreIndex = []
countIndex = []

for score in scoreList :
    if score > 530 :
        scoreIndex.append(scoreList.index(score))


for i in range(0, 91) :
    if countList[i] >= 4 :
        countIndex.append(i)

print(scoreIndex)
print(countIndex)

for index in scoreIndex :
    print(scoreList[index])
for index in countIndex :
    print(countList[index])

t1 = np.arange(0, 91, 1)

plt.figure(1)
plt.title('Wave Point')
plt.plot(t1, countList, c = 'g', lw = 1, ls = ':')
plt.xlabel('day')
plt.ylabel('point( /4)')
plt.legend()

plt.figure(2)
plt.title('Wave Score')
plt.plot(t1, scoreList, c = 'b', lw = 1, ls = '--')
plt.xlabel('day')
plt.ylabel('score( /550)')
plt.legend()
plt.show()




