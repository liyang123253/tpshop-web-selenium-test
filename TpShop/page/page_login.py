from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import Utils
from base.base import PageBase
from config import *

class PageLogin(PageBase):


    def __init__(self, driver):
        # 获取driver对象
        # driver = Utils.get_driver()
        super().__init__(driver)
        # 设置页面实例属性
        self.username = (By.ID,"username")
        self.password = (By.ID,"password")
        self.verify_code = (By.ID,"verify_code")
        self.login_button = (By.NAME,"sbtbutton")
        # 成功结果的元素属性
        self.success_result = (By.CSS_SELECTOR,".mu-m-phone")
        # 失败结果元素属性
        self.fail_result = (By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding")


    def open_url(self):
        self.driver.get(BASE_URL)

    def login(self,username,password,verify_code):
        self.base_put(self.username,username)

        self.base_put(self.password,password)

        self.base_put(self.verify_code,verify_code)

        self.base_click(self.login_button)
        # ele1 = self.fd_element(self.username)
        # ele1 = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.username))
        # ele1.clear()
        # ele1.send_keys("13800000111")
        # self.driver.find_element(*self.username).send_keys("13800000111")
        # ele2 = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.password))
        # ele2.clear()
        # ele2.send_keys("123456")
        # ele3 = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.verify_code))
        # ele3.clear()
        # ele3.send_keys("8888")
        # self.driver.find_element(*self.verify_code).send_keys("8888")
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.login_button)).click()
        # self.driver.find_element(*self.login_button).click()
        # self.base_click(self.login_button)
        time.sleep(2)


    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text

# if __name__ == "__main__":
#     driver = PageLogin(Utils.get_driver())
#     driver.open_url()
#     driver.login("13800000141","123456","8888")








