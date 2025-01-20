import os

class SetEmailPass:
    def __init__(self):
        self.email = None
        self.password = None

    def check_and_set(self):
        # Check for BBY_EMAIL and BBY_PASS
        self.email = os.getenv("BBY_EMAIL")
        self.password = os.getenv("BBY_PASS")

        if not self.email or not self.password:
            print("Environment variables not set.")
            self.email = input("Enter your Best Buy email: ")
            self.password = input("Enter your Best Buy password: ")

            # Set environment variables for the session
            os.environ["BBY_EMAIL"] = self.email
            os.environ["BBY_PASS"] = self.password
            print("Environment variables set for this session.")

        else:
            print(f"Using existing environment variables:\nBBY_EMAIL: {self.email}\nBBY_PASS: {self.password}")

        return self.email, self.password
    
# This block only runs if the file is executed directly
if __name__ == "__main__":
    email_pass_manager = SetEmailPass()
    email_pass_manager.check_and_set()