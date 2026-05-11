from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.mark.parametrize('creds')

def test_login(creds):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://account.reebok.com/authentication/login?client_id=4c81cce5-1fbd-445b-b270-d7a18015500c&locale=en-US&redirect_uri=%2Fauthentication%2Foauth%2Fauthorize%3F_cs%3D3AMP.S_AMER_f_f_-%252AWOI8ZxTzmMNeGYezFbkA%26buyer_flags%3DeyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhYmctcmVlYm9rLXN0b3JlLm15c2hvcGlmeS5jb20iLCJmbGFncyI6W10sImV4cCI6MTc3ODg3MzIxNywibmJmIjoxNzc4MjY4NDE3fQ.naPmFFskjlxvGmtjeEHm529ouK62Zxh4auSW4MIDNho%26client_id%3D4c81cce5-1fbd-445b-b270-d7a18015500c%26locale%3Den-US%26nonce%3D7b0300bc-4b4f-42c3-afb7-85828721d5f1%26redirect_uri%3Dhttps%253A%252F%252Fwww.reebok.com%252Fcustomer_authentication%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2Bemail%2Bcustomer-account-api%253Afull%26state%3DhWNBw6RlnM4jmrrVpPkVWzXV")
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys('user.com')
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div/main/div[4]/div/form/div[1]/div/div/button").click()
    element = driver.find_element(By.ID, "error-for-customer-authentication-web-email")

    # Assert the text is "test"
    assert element.text == "Enter a valid email address"
    driver.quit()


















