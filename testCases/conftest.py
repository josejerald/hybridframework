import pytest
from selenium import webdriver
@pytest.fixture()
def access_login_page(browser):
    if (browser == "chrome" ):
        return webdriver.Chrome()
    elif (broswer == "firefox" or browser == "ff"):
        return webdriver.Firefox()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--env", action="store", default="QA")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def environment(request):
    return request.config.getoption("--env")

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Demo Project'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Jerald'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)