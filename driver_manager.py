from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import os

class DriverManager:
    def __init__(self):
        self.driver = None

    def create_driver(self):
        # Initialize the WebDriver with undetected_chromedriver
        self.driver = uc.Chrome() #headless=True
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