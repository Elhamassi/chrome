import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from pytesseract import image_to_string 
from PIL import Image



class ChromeVersion(object):
    driver = None;
    ###
    ###
    def drivers(self):
        chrome = Options()
        chrome.add_argument('--no-sandbox')
        chrome.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\IT\Desktop\chrome\drivers\chromedriver.exe',chrome_options=chrome)
        
        # navigate to the url
        self.driver.get("https://chercher.tech/python/windows-selenium-python");
        # get the Session id of the Parent
        parentGUID = self.driver.current_window_handle;
        # click the button to open new window
        self.driver.find_element_by_id("two-window").click();
        time.sleep(5000);
        # get the All the session id of the browsers
        allGUID = self.driver.window_handles;
        # pint the title of th epage
        print("Page title before Switching : "+ self.driver.getTitle());
        print("Total Windows : "+allGUID.size());
        # iterate the values in the set
        for guid in allGUID:
            # one enter into if blobk if the GUID is not equal to parent window's GUID
            if(guid != parentGUID):
                # switch to the guid
                self.driver.switch_to_window(guid);
                # break the loop
                break;


        # search on the google page
        self.driver.find_element_by_name("q").send_keys("success");
        # print the title after switching
        print("Page title after Switching to goolge : "+ self.driver.getTitle());
        time.sleep(5000);
        # close the browser
        self.driver.close();
        # switch back to the parent window
        self.driver.switch_to_window(parentGUID);
        # print the title
        print("Page title after switching back to Parent: "+ self.driver.getTitle());
        
        
    def captcha(self):
        # display = Display(visible=0, size=(800, 600))
        # display.start()
        try:
            chrome = Options()
            # chrome.add_argument('--headless')
            chrome.add_argument('--no-sandbox')
            chrome.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome(executable_path=r'C:\Users\IT\Desktop\chrome\drivers\chromedriver.exe',chrome_options=chrome) 

            ##########
            self.driver.get('https://account.microsoft.com/profile/edit-name')
            # self.driver.set_window_size(1120, 550)
            time.sleep(10)
            
            #### AUTH
            self.driver.find_element_by_css_selector('#i0116').send_keys("hamassiyou@hotmail.com")
            self.driver.find_element_by_css_selector("#idSIButton9").click()
            time.sleep(6)
            self.driver.find_element_by_css_selector('#i0118').send_keys("Yousra12345678")
            self.driver.find_element_by_css_selector("#idSIButton9").click()
            time.sleep(8)
            
            self.driver.save_screenshot('screenshot1.png')
            element = self.driver.find_element_by_xpath('//div[@id="captcha-challenge-holder"]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr/td/img[1]')
            self.driver.execute_script("arguments[0].scrollIntoView();" ,element)
            time.sleep(10)
            self.driver.save_screenshot('screenshot2.png')
            
            return True
        except Exception as e:
            print(e)
            return False

APP = ChromeVersion()
status = APP.drivers()
print(status)


























