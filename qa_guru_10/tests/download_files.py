import time
import allure_pytest
import requests
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# download with api
url = "https://raw.githubusercontent.com/pytest-dev/pytest/main/doc/en/img/pytest_logo_curves.svg"

response = requests.get(url)
content = response.content

with open("new_image.svg", 'wb') as file:
    file.write(content)

# download with selenium webdriver
download_button = '[data-testid="download-raw-button"]'
browser_url = "https://github.com/pytest-dev/pytest/blob/main/README.rst"

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": r"C:\Users\User\qa_guru_10\qa_guru_10\tests",
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

driver_binary_path = ChromeDriverManager().install()
# service = Service(driver_binary_path, options=options)
driver = webdriver.Chrome(service=Service(driver_binary_path), options=options)
browser.config.driver = driver

browser.open(browser_url)
browser.element(download_button).click()
time.sleep(4)

with open("README.rst") as file:
    assert "framework makes it easy to write small tests" in file.read()