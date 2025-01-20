from setup_env import setup_environment
from driver_manager import DriverManager
from bby_signin import sign_in
from bby_product_buynow import buy_product
from setEmailPass import SetEmailPass

# List of product URLs
PRODUCT_URLS = [
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-5080-16gb-gddr7-graphics-card-gun-metal/6614153.p?skuId=6614153",
    "https://www.bestbuy.com/site/nvidia-geforce-rtx-5090-32gb-gddr7-graphics-card-dark-gun-metal/6614151.p?skuId=6614151"
]

def main():
    # Step 1: Set Email and Password
    print("Checking and setting environment variables for email and password...")
    email_pass_manager = SetEmailPass()
    BBY_EMAIL, BBY_PASS = email_pass_manager.check_and_set()

    # Step 2: Run setup_env
    print("Running environment setup...")
    setup_environment()

    # Step 3: Initialize Driver
    manager = DriverManager()
    driver = manager.create_driver()

    try:
        # Step 4: Sign In
        print("Signing in...")
        sign_in(driver, BBY_EMAIL, BBY_PASS)

        # Step 5: Attempt to buy products
        buy_product(driver, PRODUCT_URLS)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        manager.quit_driver()

if __name__ == "__main__":
    main()
