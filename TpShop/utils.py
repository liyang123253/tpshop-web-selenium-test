import json
import logging
from logging import handlers
from colorama.ansi import clear_screen
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import PATH


class Utils:


    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Edge()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(5)
        return cls.driver



    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


def read_json(file_name):

    # 读取json文件并转化为[(),(),(),...]的列表
    data = []
    file_path = PATH + "/data/" + file_name
    with open(file_path,mode='r',encoding='utf-8') as f:
        # 读取json文件并解析为python对象
        tmp = json.load(f)
        for i in tmp:
            a = tuple(i.values())
            data.append(a)
        return data


class GetLog:

    __log = None
    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = PATH + "/log/" + "web.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename = filename, #日志文件名
                                                           when = "midnight",  #日志归档时间
                                                           interval = 1,    #每天归档一次
                                                           backupCount = 3, #保留三天日志
                                                           encoding = "utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s]"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log