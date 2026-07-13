from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from base.base import PageBase


class PageAddress(PageBase):

    def __init__(self, driver):

        super().__init__(driver)

        self.account_set = (By.CSS_SELECTOR,"div.u-dt > span")
        self.address_set = (By.LINK_TEXT,"收货地址")
        self.address_add = (By.CSS_SELECTOR,".co_blue")
        self.people = (By.CSS_SELECTOR,".invoice_tt")
        self.phone = (By.NAME,"mobile")
        self.province = (By.ID,"province")
        self.city = (By.ID,"city")
        self.district = (By.ID,"district")
        self.address = (By.NAME,"address")
        self.save_bt = (By.ID,"address_submit")
        # 添加地址成功需要断言的元素属性
        self.success_result = (By.CLASS_NAME,"sx2")
        #添加地址失败的元素属性
        self.fail_result = (By.ID,"err_consignee")


    def add_address(self,people,phone,address,province,city,district):

        self.mouse_move(self.account_set)
        self.base_click(self.address_set)
        self.driver.refresh()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.base_click(self.address_add)
        self.base_put(self.people,people)
        self.base_put(self.phone,phone)
        self.select_choose(self.province,province)
        self.select_choose(self.city,city)
        self.select_choose(self.district,district)
        self.base_put(self.address,address)
        self.base_click(self.save_bt)



    def get_success_result(self):
        return self.fd_element(self.success_result).text


    def get_fail_result(self):
        return self.fd_element(self.fail_result).text




