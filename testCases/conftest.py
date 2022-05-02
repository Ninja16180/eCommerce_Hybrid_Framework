from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

#Run this command on CLI to specify which browser to use:
#pytest -s -v -n=2 testCases/test_login.py --browser <browser name:chrome/firefox>

#Run this command on CLI to run testing on multiple browsers in parallel:
#pytest -s -v -n=2 testCases/test_login.py --browser <browser name:chrome/firefox>
#pytest -s -v -n=2 testCases/ --browser <browser name:chrome/firefox> <--This will run all the test cases inside the 'testCases' folder
#where n is the number of methods in the testcase file
#pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome  #-m for marker, "sanity or regression" means tests markered either sanity or regression\
# will be executed. "sanity and regression" tests have to have both sanity and regression markers

@pytest.fixture()
def setup(browser):

    if browser=='chrome':
        driver = webdriver.Chrome(executable_path=r"C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/chromedriver.exe")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path=r"C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/geckodriver.exe")
    else:
        # setting up chrome as default browser if by mistake no browser type is specified in CLI command
        driver = webdriver.Chrome(
            executable_path=r"C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/chromedriver.exe")

    #s = Service('C:/Users/dips2/Documents/Dipanjana/Preperation/Testing/selenium/drivers/chromedriver.exe')
    #driver = webdriver.Chrome(service=s)
    #url = 'https://www.google.com'
    #browser.get(url)
    return driver

def pytest_addoption(parser):  #This will get value from the command prompt
    parser.addoption(parser)

@pytest.fixture(scope="session")
def browser(request):  #This will return the browser value to the setup() method above
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# IMP: CLI command to generate HTML report :
# pytest -s -v -n=2 --html=Reports\report.html testCases/test_login.py --browser <browser name:chrome/firefox>

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Dipanjana'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)