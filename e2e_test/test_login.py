from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..server.url_adress import url

def test_login():
    driver = Chrome()
    try:
        driver.get(url + 'login')
        input_username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
        input_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        input_username.send_keys("admin")
        input_password.send_keys("root")

        login_form = driver.find_element(By.ID, "login-form")
        login_form.submit()

        if 'authorized' in driver.page_source:
            assert True
        else:
            assert False
    finally:
        driver.close()
