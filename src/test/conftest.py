import pytest
from selenium import webdriver
from pathlib import Path

@pytest.fixture(scope="class")
def setup(request):
    url="https://opensource-demo.orangehrmlive.com/"
    driver=webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()


def getChromePath():
    root=Path("chrome").resolve()
    path=str(root)+"/chromedriver147"
    print("chrome path is:: ",path)
    return path


