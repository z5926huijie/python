import pprint
from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\huijie\Documents\WeChat Files\zhangyuhp\Files\chromedriver')
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
ret = driver.find_element_by_id('forecastID')
#print(ret.text)
lines=ret.text
line= lines.split('\n')
#city = []
weatherlist=[]
dictret = {}
#num=0
for one in line:
    if '/'not in one:
        city = one
        #city.append(one)
    else:
        weather = one.split('/')[0].split('℃')[0]
        weather1 = one.split('/')[1].split('℃')[0]
        weather =int(weather)
        weather1 = int(weather1)
        weatherlist.append(weather)
        weatherlist.append(weather1)
        if city not in dictret:
            dictret[city]=[]
        dictret[city].append(weather)
minv = min(weatherlist)
#print(minv)
#print(dictret)
for (k,v) in dictret.items():
    v=v[0]
    if v==minv:
        #print(v)
        #print(k)
        print('最低温度的城市：%s，最低温度'%k,v)

# for i in dictret[city]:
#     i=i.split('/')[0].split('℃')[0]
#     print(i)
#     i = int(i)
#     # if theMin >i:
#     #     theMin =i
# print(i)

driver.quit()