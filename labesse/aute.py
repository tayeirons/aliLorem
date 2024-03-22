from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

agree_btn_2 = (By.XPATH, '//button[contains(text(), "I agree")]')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(agree_btn_2)
).click()
