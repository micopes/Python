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
    a = (33 - windspeed) * 5 # 풍속1f
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
#score

plt.figure(2)
plt.title('Wave Score')
plt.plot(t1, scoreList, c = 'b', lw = 1, ls = '--')
plt.xlabel('day')
plt.ylabel('score( /550)')
plt.legend()
plt.show()


