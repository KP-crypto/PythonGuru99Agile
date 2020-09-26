import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    elif browser=="firefox":
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

