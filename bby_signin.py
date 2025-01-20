from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random

# Best Buy homepage URL
BBY_HOME_URL = "https://www.bestbuy.com/"

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

    # Add a short delay after typing the full password
    time.sleep(1)

    ###THIS SECTION NEEDS RETRIES SINCE THE BOT FLAGGING POPS UP AN ERROR MESSAGE###

    timeout = 20 #setting the timeout amount
    start_time = time.time() #recording start time
    
    while time.time() - start_time < timeout:
        try:
            print("Clicking 'Continue' button...")
            continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'cia-form__controls__submit') and text()='Continue']")))
            continue_button.click()

            # Check for "Something went wrong" message
            time.sleep(3)
            error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'something went wrong')]")
            print("Detected error: 'Something went wrong'. Retrying...")
        except NoSuchElementException:
            print("'Continue' button clicked successfully!")
            break
        except Exception as e:
            print(f"Error while clicking 'Continue' button: {e}")

    # # Locate and click the "Continue" button
    # print("Locating the 'Continue' button...")
    # continue_button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'cia-form__controls__submit') and text()='Continue']"))
    # )
    # continue_button.click()





    # Verify sign-in
    print("Verifying sign-in...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "account-menu-account-button"))
    )
    print("Sign-in successful!")