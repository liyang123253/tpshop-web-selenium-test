import time

from page.page_login import PageLogin
from utils import Utils, GetLog
from script import *

class TestLogin:


    def setup_method(self):
        driver = Utils.get_driver()
        self.page_login = PageLogin(driver)
        self.page_login.open_url()
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)


    def teardown_method(self):

        Utils.quit_driver()

    def test_01_login_success(self):
        # 准备
        # driver = Utils.get_driver()
        # page_login = PageLogin(driver)
        # # 调用方法
        # page_login.open_url()
        # page_login.login("13800000141","123456","8888")
        self.page_login.login("13800000141", "123456", "8888")
        # 打印日志
        result = self.page_login.get_success_result()
        log.info(f"登录结果:{result}")
        # 断言
        assert "13800000141" == result
        # 退出浏览器
        # Utils.quit_driver()

    def test_02_login_fail_pwd_error(self):
        # 准备
        # driver = Utils.get_driver()
        # page_login = PageLogin(driver)
        # # 调用方法
        # page_login.open_url()
        self.page_login.login("13800000141", "1234", "8888")
        # 打印日志
        result = self.page_login.get_fail_result()
        log.info(f"登录结果:{result}")
        # 断言
        assert "密码错误" in result
        # 退出浏览器
        # Utils.quit_driver()

    def test_03_login_fail_phone_none(self):
        self.page_login.login(" ", "123456", "8888")
        result = self.page_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert "用户名不能为空" in result

    def test_04_login_fail_password_none(self):
        self.page_login.login("13800000141", " ", "8888")
        result = self.page_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert "密码不能为空" in result

    def test_05_login_fail_code_none(self):
        self.page_login.login("13800000141", "123456", " ")
        result = self.page_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert "验证码不能为空" in result