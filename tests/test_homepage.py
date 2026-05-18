from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("http://20.17.145.40")

time.sleep(3)

assert "Ice" in driver.page_source

print("Homepage Test Passed")

driver.quit()