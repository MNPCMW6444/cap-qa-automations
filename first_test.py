import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_user_can_use_app(self):
        driver = self.driver
        driver.get("https://app.caphub-funding.com")

        wait = WebDriverWait(driver, 10)  # 10 seconds timeout
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="email"]')))
        password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="password"]')))
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="login-button"]')))
        actions = ActionChains(driver)
        actions.move_to_element(login_button).click().perform()

        email.send_keys(Keys.CONTROL + "a")
        
        email.send_keys("flighter98311+1@gmail.com")  
        password.send_keys("daniel1998$&@")  
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="login-button"]')))
        actions = ActionChains(driver)
        actions.move_to_element(login_button).click().perform()
        time.sleep(15)  # Wait for the page to load

        # Check the result (replace with your app's specific result checks)
        result_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='home']")))
        self.assertEqual(result_element.text, "home")


def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
