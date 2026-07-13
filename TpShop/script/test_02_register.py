from page.page_register import PageRegister
from utils import Utils
from script import *
import time

class TestRegister:

    def setup_method(self):
        driver = Utils.get_driver()
        self.page_register = PageRegister(driver)
        self.page_register.open_url()


        driver.refresh()
        time.sleep(2)
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

    def test_01_register_success(self):

        self.page_register.register("13800000018","8888","123456","123456")

        result = self.page_register.get_success_result()
        log.info(f"注册结果: {result}")

        assert "我的订单" == result

    def test_02_register_fail_phone_error(self):

        self.page_register.register("1380000014","8888","123456","123456")

        result = self.page_register.get_fail_result()
        log.info(f"注册结果: {result}")

        assert "输入正确手机号" in result

    def test_03_register_fail_code_none(self):

        self.page_register.register("13800000003","7777","123456","123456")

        result = self.page_register.get_fail_result()
        log.info(f"注册结果: {result}")

        assert "验证码错误" in result

    def test_04_register_fail_pwd_number_error(self):
        self.page_register.register_pwd_error("13800000004","8888","12345")

        result = self.page_register.get_fail_result()
        log.info(f"注册结果: {result}")

        assert "密码有效长度为6-16位" in result

    def test_05_register_fail_pwd_pwd2_error(self):
        self.page_register.register("13800000005","8888","123456","1234567")

        result = self.page_register.get_fail_result()
        log.info(f"注册结果: {result}")

        assert "两次密码不一致" in result

    def test_06_register_fail_phone_exist(self):
        self.page_register.register("13800000141","8888","123456","123456")

        result = self.page_register.get_fail_result()
        log.info(f"注册结果: {result}")

        assert "手机号已注册" in result



