import time
from base.base import PageBase
from selenium.webdriver.common.by import By
from utils import Utils


class PageRegister(PageBase):


    def __init__(self, driver):
        # driver = Utils.get_driver()
        super().__init__(driver)
        self.username = (By.ID,"username")
        self.verify_code  = (By.NAME,"verify_code")
        self.password = (By.ID,"password")
        self.password2 = (By.ID,"password2")
        self.invite = (By.NAME,"invite")
        self.registerbt = (By.LINK_TEXT,"同意协议并注册")
        # 注册成功后跳转到首页的元素属性
        self.success_result = (By.LINK_TEXT,"我的订单")
        # 手机号格式错误的元素属性
        self.fail_result = (By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding")

    # 打开注册页面
    def open_url(self):
        self.driver.get("https://hmshop-test.itheima.net/Home/User/reg.html")
        time.sleep(5)

    # 查找元素注册
    def register(self,username,verify_code,password,password2):
        self.base_put(self.username,username)
        self.base_put(self.verify_code,verify_code)
        self.base_put(self.password,password)
        self.base_put(self.password2,password2)
        self.base_click(self.registerbt)


    def register_pwd_error(self,username,verify_code,password):
        self.base_put(self.username,username)
        self.base_put(self.verify_code,verify_code)
        self.base_put(self.password,password)
        self.base_click(self.password2)



    def get_success_result(self):
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text

# if __name__ == "__main__":
#     driver = PageRegister()
#     driver.open_url()
#     driver.register()



