import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://20.17.145.40")
    time.sleep(3)  # Brief wait for page stability

    # Handle iframe if your environment uses it
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if iframes:
        driver.switch_to.frame(iframes[0])

    # CLEAN FIX: Target the input tag where the value attribute starts with 'Place Order'
    button = driver.find_element(By.CSS_SELECTOR, "input[value^='Place Order']")

    assert button is not None
    print("Place Order Button Found - Test Passed")

finally:
    driver.quit()