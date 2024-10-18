from time import sleep
from selenium.webdriver import ActionChains, Keys
from . import constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
chrome_options.add_extension(const.EXTENSION_PATH)

class InternetSpeedTwitterBot(webdriver.Chrome):
    def __init__(self, teardown=False):
        super().__init__(service=service, options=chrome_options)
        self.down = const.PROMISED_DOWN
        self.up = const.PROMISED_UP
        self.teardown = teardown
        self.implicitly_wait(40)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def get_internet_speed(self):
        """Get the internet speed."""
        self.get("https://www.speedtest.net/")
        sleep(3)
        go_button = self.find_element(
            By.CLASS_NAME,
            value="start-text"
        )
        go_button.click()
        sleep(60)
        down_speed = self.find_element(
            By.CLASS_NAME,
            value="download-speed"
        )
        self.down = float(down_speed.text)
        up_speed = self.find_element(
            By.CLASS_NAME,
            value="upload-speed"
        )
        self.up = float(up_speed.text)

    def on_browsec_vpn(self):
        self.get("chrome-extension://omghfjlpggmjjaagoclmmobgdodcjboh/popup/popup.html")
        # Create an instance of ActionChains
        actions = ActionChains(self)
        # Perform TAB and ENTER key
        for _ in range(3):
            sleep(1)
            actions.send_keys(Keys.TAB).perform()
        sleep(1)
        actions.send_keys(Keys.ENTER).perform()
        self.find_element(By.XPATH, '/html/body/div[2]').click()
        sleep(2)

    def tweet_at_provider(self):
        if self.down >= const.PROMISED_DOWN and self.up >= const.PROMISED_UP:
            print('Internet speed is good.')
            return
        self.get("https://twitter.com/login")
        sleep(3)
        username = self.find_element(
            By.CSS_SELECTOR,
            value='input[autocomplete="username"]'
        )
        username.send_keys(const.TWITTER_USERNAME)
        next_button = self.find_element(By.XPATH, '//span[contains(text(), "Next")]')
        next_button.click()
        # This exception handling is to check if the unusual login warning is present
        try:
            self.find_element(
                By.XPATH,
                value='//span[contains(text(), "Enter your phone number")]'
            )
        except:
            print('There is no unusual login warning.')
        else:
            email_entry = self.find_element(By.TAG_NAME, 'input')
            email_entry.send_keys(const.TWITTER_EMAIL)
            next_button = self.find_element(
                By.XPATH,
                value='//span[contains(text(), "Next")]')
            next_button.click()

        password_entry = self.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
        password_entry.send_keys(const.TWITTER_PASSWORD)
        login_button = self.find_element(
            By.XPATH,
            value='//span[contains(text(), "Log in")]'
        )
        login_button.click()
        # noinspection PyBroadException
        try:
            cookies_rejection_button = self.find_element(
                By.XPATH,
                value= '//span[contains(text(), "Refuse")]'
            )
        except Exception:
            print('There is no cookies pop-up.')
        else:
            cookies_rejection_button.click()
        sleep(3)
        tweet_button = self.find_element(
            By.CSS_SELECTOR,
            value='a[data-testid="SideNav_NewTweet_Button"]'
        )
        tweet_button.click()
        sleep(7)
        text_message = (f"Hey Internet Provider @eduroam, why is my internet speed {self.down}down/{self.up}up"
                        f" when I pay for {const.PROMISED_DOWN}down/{const.PROMISED_UP}up?")
        tweet_text_area = self.find_element(
            By.CSS_SELECTOR,
            value='div[data-testid="tweetTextarea_0"]'
        )
        tweet_text_area.send_keys(text_message + '\n')
        sleep(3)
        tweet_button = self.find_element(
            By.XPATH,
            value='//span[contains(text(), "Post")]'
        )
        tweet_button.click()



