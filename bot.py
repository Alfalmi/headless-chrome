from selenium import webdriver
from time import sleep
#from fake_useragent import UserAgent

#ua = UserAgent()
#userAgent = ua.random
#print(userAgent)

class MyBot:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/ 85.0.41.83 Safari/537"

        self.options =webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument('--window-size-1920, 1080')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--proxy-server="direct://"')
        self.options.add_argument('--proxy-bypass-list=*')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
MyBot()
   