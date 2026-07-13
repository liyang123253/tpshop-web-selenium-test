# tpshop-web-selenium-test
###  项目结构
```
e:\TpShop/
├── config.py              # 项目配置（URL地址等）
├── utils.py               # 工具类（驱动管理、日志、数据读取）
├── pytest.ini             # pytest 配置文件
├── base/
│   └── base.py            # 基础页面类（封装通用操作）
├── page/
│   ├── page_login.py      # 登录页面封装
│   ├── page_register.py   # 注册页面封装
│   └── page_address.py    # 收货地址页面封装
├── script/
│   ├── test_01_login.py   # 登录功能测试用例
│   ├── test_02_register.py # 注册功能测试用例
│   └── test_03_address.py  # 收货地址功能测试用例
├── log/                   # 日志文件
└── report/                # Allure 测试报告
```
### 🛠 技术栈
组件 说明 Python 编程语言（3.14版本） Selenium Web 自动化测试框架（使用 Edge 浏览器） pytest 测试执行框架 Allure 测试报告生成工具 Page Object Model 页面对象模型设计模式


## ✅ 测试功能

### 1. 登录模块
- ✅ 登录成功
- ✅ 密码错误登录失败
- ✅ 用户名为空登录失败
- ✅ 密码为空登录失败
- ✅ 验证码为空登录失败

### 2. 注册模块
- ✅ 注册成功
- ✅ 手机号格式错误注册失败
- ✅ 验证码错误注册失败
- ✅ 密码长度不足注册失败
- ✅ 两次密码不一致注册失败
- ✅ 手机号已注册注册失败

### 3. 收货地址模块
- ✅ 添加地址成功
- ✅ 收货人姓名为空添加失败

## 🚀 环境要求

1. **Python 3.14+**
2. **Edge 浏览器**（已安装）
3. **EdgeDriver**（需与 Edge 版本匹配）


## 🔍 运行测试

```bash
# 运行所有测试用例（生成 Allure 报告）
pytest

# 运行指定测试模块
pytest script/test_01_login.py

# 运行单个测试用例
pytest script/test_01_login.py::TestLogin::test_01_login_success

# 生成并查看 Allure 报告
allure serve report
```

## 🎨 设计模式

项目采用 Page Object Model (POM) 设计模式：

1. BasePage ( base/base.py ) - 封装通用操作：
   
   - 元素定位 ( fd_element )
   - 输入文本 ( base_put )
   - 点击操作 ( base_click )
   - 截图、切换窗口/框架、鼠标悬浮、下拉框选择等
2. Page类 ( page/ ) - 每个页面独立封装：
   
   - 页面元素定位器
   - 页面业务方法
3. Test类 ( script/ ) - 测试用例：
   
   - setup_method : 初始化浏览器、打开页面
   - teardown_method : 关闭浏览器
   - 具体测试方法

## 📝 配置说明

### pytest.ini

```ini
[pytest]
addopts = -s --alluredir report --clean-alluredir
testpaths = ./script
python_files = test*.py
python_classes = Test*
python_functions = test*
```

### config.py

```python
BASE_URL = "https://hmshop-test.itheima.net/Home/user/login.html"  # 前台地址
```

## ⚠️ 注意事项

1. 测试环境为线上测试地址：`https://hmshop-test.itheima.net`
2. 确保 Edge 浏览器版本与 EdgeDriver 版本匹配
3. 验证码默认使用 `8888`（测试环境通用验证码）
4. 测试账号：`13800000141`，密码：`123456`
5. 测试用例中的账号可能会过期，请及时更换



