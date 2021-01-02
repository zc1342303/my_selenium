from selenium import webdriver
import requests

from ocr import OCR


class Controller:
    def __init__(self):
        # 启动浏览器，打开指定网页
        opt = webdriver.ChromeOptions()  # 创建浏览器
        # opt.set_headless()                            #无窗口模式
        driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
        driver.get('http://58.215.18.81:32314/dwz_springmvc/login')  # 打开网页
        # driver.maximize_window()                      #最大化窗口
        driver.set_window_size(1200, 800)
        self.ocr = OCR()

        self.driver = driver

    def login(self, user, password):
        self.driver.find_element_by_xpath('/html/body/article/div/div/div/form/div/div[1]/input').send_keys(user)
        self.driver.find_element_by_xpath('/html/body/article/div/div/div/form/div/div[2]/input').send_keys(password)
        elem = self.driver.find_element_by_xpath('//*[@id="img_val"]')
        self.ocr.get_img(self.driver, elem)
        res = self.ocr.run()
        self.driver.find_element_by_xpath('//*[@id="txtCode"]').send_keys(res)
        self.driver.find_element_by_xpath('//*[@id="BtnSave"]').click()
