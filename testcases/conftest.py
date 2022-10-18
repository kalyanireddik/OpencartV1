import os.path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
@pytest.fixture()
def setup():
    if browser =='edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("lunching edge browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("lunching firefox browser...")
    else:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        print("lunching chrome browser...")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##### pytest HTML reports #####
# it is hook for adding environmentinfo to html
def pytest_configure(config):
    config._metadata["Project Name"]='Opencart'
    config._metadata["Modul Name"] ='CustRegistration'
    config._metadata["Tester"] = 'Kalyani'


# it is hook for remove\modify environmentinfo to html
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA-HOME",None)
    metadata.pop("Plugins",None)

#specifiying report folder loctionand save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

















