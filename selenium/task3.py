import pprint
from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\huijie\Documents\WeChat Files\zhangyuhp\Files\chromedriver')
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
ret = driver.find_element_by_id('forecastID')
#print(ret.text)
lines=ret.text
line= lines.split('\n')
lowestcity=[]

weathermin=100
for one in line:
    if '/'not in one:
        curcity = one
    else:
        weather = one.split('/')[0].split('℃')[0]
        weather =int(weather)
        if weather<weathermin:
            weathermin=weather
            lowestcity=[curcity]
        elif weather==weathermin:
            lowestcity.append(curcity)
print('温度最低为%s℃,城市有：%s'%(weathermin,''.join(lowestcity)))


driver.quit()