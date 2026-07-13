import os

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import PATH
from utils import Utils, GetLog


class PageBase(object):



    def __init__(self,driver,timeout = 10):
        self.driver = driver     #相当于self.driver = Utils.get_driver()
        self.default_timeout = timeout  #默认等待时间


    def fd_element(self,loc):

        # loc元素定位方式及属性
        try:
            element = WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(loc))
            return element
        except Exception as e:
            GetLog.get_log().error(f"元素定位超时,定位信息:{loc},错误情况:{e}")
            raise



    def base_put(self,loc,text):
        ele = self.fd_element(loc)
        ele.clear()
        ele.send_keys(text)

    def base_click(self,loc):
        self.fd_element(loc).click()

    # 截图
    def get_shot(self,file_name):
        file_path = os.path.join(PATH,'img',file_name)
        self.driver.get_screenshot_as_file(file_path)


    def base_switch_handle(self,loc):
        WebDriverWait(self.driver, self.default_timeout).until(lambda x: len(x.window_handles) > 1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        ele = self.fd_element(loc)
        return ele

    def base_switch_frame(self,loc):
        frame_ele = self.fd_element(loc)
        self.driver.switch_to.frame(frame_ele)


    def base_default_frame(self,loc):
        self.driver.switch_to.default_content()

    # 鼠标悬浮
    def mouse_move(self,loc):
        ele = self.fd_element(loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    # 下拉框选择
    def select_choose(self,loc,value):
        ele = self.fd_element(loc)
        select = Select(ele)
        select.select_by_value(value)
