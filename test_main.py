
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



def test_open(driver):
    driver.get("https://www.demoblaze.com/")
    galaxy_x6 = driver.find_element(By.XPATH, '//*[@id="itemc"]')
    galaxy_x6.click()
