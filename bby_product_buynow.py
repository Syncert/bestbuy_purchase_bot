from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#TODO: Add methods that simulate human behavior. I.E Scrolling, Refresh random intervals, etc.

def buy_product(driver, urls):
    """
    Monitors each URL in the provided list of product URLs using separate tabs.
    Each tab refreshes every 60 seconds if the 'Buy Now' button is not available.
    """
    # Open a tab for each URL
    for index, url in enumerate(urls):
        if index == 0:
            # Use the current tab for the first URL
            driver.get(url)
        else:
            # Open a new tab for subsequent URLs
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
        print(f"Opened tab {index + 1} for: {url}")

    # Monitor all tabs
    while True:
        for index, url in enumerate(urls):
            try:
                # Switch to the correct tab
                driver.switch_to.window(driver.window_handles[index])
                print(f"Monitoring tab {index + 1}: {url}")

                # Look for the "Buy Now" button
                buy_now_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-button-state, 'ADD_TO_CART') and contains(text(), 'Buy Now')]"))
                )
                buy_now_button.click()
                print(f"'Buy Now' button clicked in tab {index + 1}!")

                # Proceed to checkout and place order
                print("Waiting for 'Place Your Order' button...")
                place_order_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-track, 'Place your Order')]"))
                )
                place_order_button.click()
                print(f"Order placed successfully for tab {index + 1}!")
                return  # Exit once an order is placed
            except Exception as e:
                print(f"Tab {index + 1} error: {e}")
                print(f"Refreshing tab {index + 1}...")
                driver.refresh()
                time.sleep(60)  # Wait 60 seconds before retrying
