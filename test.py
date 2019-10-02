
from selenium import webdriver
#importing webdriver and selenium


#chrome driver path from an chromewebdriver
driver = webdriver.Chrome("C:\\Users\\Brunda\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
#from driver function get the youtube page
driver.get('http://youtube.com/')
# maximise the size of the window
driver.maximize_window()

