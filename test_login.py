#Implementation of Selenium test automation for this Selenium Python Tutorial
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()
    
    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()
    
    sleep(2)
    chrome_driver.close()
