import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

SIMILAR_ACCOUNT = "math.animations" # example account
USERNAME = "**********"
PASSWORD = "***********"
url = 'https://www.instagram.com/accounts/login/'

class InstaFollower:
    def __init__(self):
        # Initialize the Chrome browser with an option to keep it open after the script finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        # Open the Instagram login page
        self.driver.get(url)
        time.sleep(5)
        # Handle cookie popup
        try:
            cookies = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
            cookies.click()
        except NoSuchElementException:
            pass

        time.sleep(5)
        # Enter the username
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(USERNAME)
        # Enter the password
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        time.sleep(3)
        # Click the login button
        log_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_button.click()

        time.sleep(10)
        # Handle saving login information popup
        try:
            save_info = self.driver.find_element(By.CSS_SELECTOR, '.x78zum5 button')
            save_info.click()
        except NoSuchElementException:
            pass

        time.sleep(5)
        # Handle notification popup
        try:
            notifications_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
            notifications_button.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        # Navigate to the specified account profile
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        time.sleep(5)
        # Click the followers link
        followers_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a"
        followers = self.driver.find_element(by=By.XPATH, value=followers_xpath)
        followers.click()
        time.sleep(5)
        # Scroll through the followers list to load more users
        scroll_window = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for _ in range(5):  # Adjust the range as needed
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_window)
            time.sleep(2)

    def follow(self):
        # Find the "Follow" buttons and click them
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.xyi19xy button')
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                # Handle cases where the "Follow" button is blocked by other pop-ups
                try:
                    ok = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
                    ok.click()
                except NoSuchElementException:
                    pass
                try:
                    cancel_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]")
                    cancel_button.click()
                except NoSuchElementException:
                    pass

instagram = InstaFollower()
instagram.login()
instagram.find_followers()
instagram.follow()
