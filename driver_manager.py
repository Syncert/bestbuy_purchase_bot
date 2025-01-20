from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class DriverManager:
    def __init__(self):
        self.driver = None

    def create_driver(self):
        # Create WebDriver with options
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Add headless mode for non-debugging
        # chrome_options.add_argument("--headless")

        # Locate the ChromeDriver
        chromedriver_path = self.find_chromedriver()

        # Initialize the WebDriver
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
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