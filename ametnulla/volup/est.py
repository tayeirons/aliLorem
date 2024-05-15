from selenium.webdriver.common.by import By

def click_Xpath(driver, index, element):
    """Clicks on the element at the given index.

    Args:
        driver: The WebDriver instance.
        index: The index of the element to click on.
        element: The element to click on.
    """

    elements = driver.find_elements(By.XPATH, element)
    elements[index].click()
