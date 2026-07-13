import time

from lx.page import driver
from page.page_address import PageAddress
from page.page_login import PageLogin
from utils import Utils
from script import *

class TestAddress:


    def setup_method(self):
        driver = Utils.get_driver()
        # 创建页面对象
        self.page_login = PageLogin(driver)
        self.address = PageAddress(driver)
        # 打开登录页面
        self.page_login.open_url()

        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        # 登录成功
        self.page_login.login("13800000141","123456","8888")

    def teardown_method(self):

        Utils.quit_driver()

    def test_01_add_address_success(self):

        self.address.add_address("收货人","13800000141","123456","1","2","3")

        result = self.address.get_success_result()
        log.info(f"新增地址结果: {result}")

        assert "收货人" in result

    def test_02_add_address_fail_people_none(self):

        self.address.add_address(" ","13800000141","123456","1","1","1")

        result = self.address.get_fail_result()
        log.info(f"新增地址结果: {result}")

        assert "收货人不能为空" in result