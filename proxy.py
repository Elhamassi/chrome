# from pyvirtualdisplay import Display
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import sys,json



class ChromeVersion(object):
    driver = None;
    ###
        
    def check(self,proxyIp):
        try:
            # display = Display(visible=0, size=(1366, 868))
            # display.start()
            
            # chrome = Options()
            # chrome.add_argument('--headless')
            # chrome.add_argument('--no-sandbox')
            # chrome.add_argument('--disable-dev-shm-usage')
            # chrome.add_argument('--proxy-server=http://'+str(proxyIp)+":3838")
            
            
            PROXY = str(proxyIp)+":3838"
            chrome_options = Options()
            chrome_options.add_argument('--proxy-server=%s' % PROXY)

            self.driver=webdriver.Chrome(executable_path=r'C:\Users\IT\Desktop\chrome\drivers\chromedriver.exe',chrome_options=chrome_options) 
            ##########
            self.driver.get("http://icanhazip.com/")
            self.driver.implicitly_wait(60)

            ##########
            elm = self.driver.find_element_by_tag_name("pre")
            print(elm.text)
            if proxyIp in elm.text:
                return True
            sys.exit()
        except Exception as e:
            print(e)
            return False

APP = ChromeVersion()
APP.check("142.4.16.247")
ips=["142.4.16.247","45.79.15.222","91.203.5.96"]
# for x in ips:
    # print(APP.check(x))


























