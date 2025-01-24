from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Best Buy homepage URL
BBY_HOME_URL = "https://www.bestbuy.com/"

def mimic_human_behavior(driver):
    # Random scrolling
    scroll_height = random.randint(200, 1000)
    driver.execute_script(f"window.scrollTo(0, {scroll_height});")
    time.sleep(random.uniform(1, 3))  # Random delay between actions


def sign_in(driver, email, password):
    """
    Signs into the Best Buy account using the provided WebDriver instance.
    """
    # Navigate to Best Buy homepage
    print("Navigating to Best Buy homepage...")
    driver.get(BBY_HOME_URL)

    # Locate and click the "Account" menu button
    print("Locating the 'Account' menu button...")
    account_menu_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "account-menu-account-button"))
    )
    account_menu_button.click()

    # Wait and locate the "Sign In" button inside the menu
    print("Locating the 'Sign In' button in the menu...")
    sign_in_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='signInButton']"))
    )
    sign_in_button.click()

    # Wait for the login form to appear
    print("Waiting for the login form...")
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fld-e"))  # Email field ID
    )

    # Populate email and proceed
    print("Filling out email...")
    for char in email:
        email_field.send_keys(char)
        time.sleep(random.uniform(0.08, 0.15))  # Random delay between 80ms and 150ms


    #click continue
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
    continue_button.click()

    # Wait and select the "Use password" option
    print("Selecting the 'Use password' option...")
    use_password_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Use password']"))
    )
    use_password_option.click()


    # Wait for the password entry field
    print("Waiting for password entry field...")
    password_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "fld-p1"))
    )

    # Enter password one character at a time
    print("Typing password...")
    for char in password:
        password_field.send_keys(char)
        time.sleep(random.uniform(0.08, 0.15))  # Random delay between 80ms and 150ms

    # # Add a short delay after typing the full password
    # time.sleep(3)

    #do random stuff
    mimic_human_behavior(driver)

    # Locate and click the "Continue" button
    print("Locating the 'Continue' button...")
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'cia-form__controls__submit') and text()='Continue']"))
    )
    continue_button.click()


    # Verify sign-in
    print("Verifying sign-in...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "account-menu-account-button"))
    )
    print("Sign-in successful!")

def monitorAndBuy(driver, urls):
    """
    Monitors each URL in the provided list of product URLs using separate tabs.
    Each tab refreshes every 60 seconds if the 'Buy Now' button is not available.
    """
    # Navigate to Best Buy homepage
    print("Navigating to Best Buy homepage...")
    driver.get(BBY_HOME_URL)

    # Open a tab for each URL
    for index, url in enumerate(urls):
        if index == 0:
            # Use the current tab for the first URL
            driver.get(url)
            time.sleep(2)  # Wait for the page to load
        else:
            # Open a new tab for subsequent URLs
            # driver.execute_script("window.open('');")
                # Opens a new tab and switches to new tab
            driver.switch_to.new_window('tab')
            time.sleep(2)  # Wait for the new tab
            driver.get(url)
            # driver.switch_to.window(driver.window_handles[-1])
        print(f"Opened tab {index + 1} for: {url}")
        print(f"{index + 1} of {len(urls)}")

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
                
                # # Close the tab
                # driver.close()
                # print(f"Closed tab {index + 1} for: {url}")

                # Remove the URL from the list
                urls.pop(index)
                print(f"Removed URL from list: {url}")

                # Switch to another open tab, if available
                if driver.window_handles:
                    #simulate human behavior
                    print("Mimicking human behavior...then switching tab")
                    mimic_human_behavior(driver)
                    driver.switch_to.window(driver.window_handles[0])
                else:
                    print("No more tabs open.")
                    return  # Exit if no tabs are left

                break  # Exit the current loop to restart the monitoring with the updated list

            except Exception as e:
                print(f"Tab {index + 1} error: {e}")
                print(f"Refreshing tab {index + 1}...")
                driver.refresh()
                time.sleep(30)  # Wait 30 seconds before retrying