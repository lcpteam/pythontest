import pytest
import os
from selenium import webdriver


@pytest.fixture(name='chrome')
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


def open_url(driver, url):
    driver.get(url)

def test_login(chrome):
    open_url(chrome, "http://www.lcptop.com/relations/")
    print("------->test_a")


if __name__ == '__main__':
     pytest.main(["-s","test_Browser.py"]) # 调用pytest的main函数执行测试
