from selenium import webdriver
import time
#引入库
usrn = input("username: ")
usrn = str(usrn)
usrp = input("password: ")
usrp = str(usrp)
#创建用户名，密码变量
driver = webdriver.Firefox()
driver.get('http://www.zhixue.com')
driver.implicitly_wait(30)
time.sleep(3)
#载入并等待加载
elem_login = driver.find_element_by_id('txtUserName')
elem_login.send_keys(usrn)
elem_login = driver.find_element_by_id('txtPassword')
elem_login.send_keys(usrp)
#输入密码
elem_login = driver.find_element_by_id('signup_button')#利用id定位登录按钮，在网页开发者模式找到
elem_login.click()
time.sleep(5)
#登录
driver.quit()
