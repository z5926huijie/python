from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\huijie\Documents\WeChat Files\zhangyuhp\Files\chromedriver')

driver.get('http://121866.com/cust/sign.html')
driver.find_element_by_id('username').send_keys('huijie')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btn_sign').click()
import time
time.sleep(2)
ret = driver.find_element_by_id('username')
print(ret.text)
if ret.text.startswith('huijie'):
    print("pass")
else:
    print('not pass')
input()
driver.quit()
