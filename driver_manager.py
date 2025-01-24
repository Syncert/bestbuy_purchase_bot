from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import os

class DriverManager:
    def __init__(self):
        self.driver = None

    def create_driver(self):
        #configure options
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--disable notifications") # Disable Popups

        #this option disables the pesky location pop ups
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.geolocation": 2,  # Block location requests
        })
        chrome_options.add_argument("--log-level=3")  # Suppress minor logs: 0=ALL, 1=INFO, 2=WARNING, 3=ERROR
        # Initialize the WebDriver with undetected_chromedriver
        self.driver = uc.Chrome(options=chrome_options) #headless=True
        return self.driver

    @staticmethod
    def find_chromedriver():
        # Dynamically locate chromedriver in PATH
        for path_dir in os.getenv("PATH").split(os.pathsep):
            chromedriver_path = os.path.join(path_dir, "chromedriver.exe")
            if os.path.isfile(chromedriver_path):
                return chromedriver_path
        raise FileNotFoundError("chromedriver.exe not found in PATH.")

    def get_driver(self):
        if self.driver is None:
            raise RuntimeError("Driver not created. Call create_driver() first.")
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None