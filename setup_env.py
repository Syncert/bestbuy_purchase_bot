import subprocess
import sys
import os
import platform

# List of required Python packages
required_packages = ["selenium", "python-dotenv"]

# Function to install Python packages
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")
        sys.exit(1)

#setup function

def setup_environment():

    # Detect OS
    os_type = platform.system()

    if os_type == "Linux":
        # Install Chromium and Chromedriver on Linux
        def install_chromium():
            try:
                print("Updating system and verifying pip is installed")
                # Update package lists and ensure pip is installed
                subprocess.check_call(["sudo", "apt-get", "update", "-y"])
                subprocess.check_call(["sudo", "apt-get", "install", "-y", "python3-pip"])

                print("Installing Chromium and Chromedriver for Linux...")
                # Install Chromium browser and Chromedriver
                subprocess.check_call(["sudo", "apt-get", "install", "-y", "chromium-browser", "chromium-chromedriver"])
                
                # Verify installation
                subprocess.check_call(["chromedriver", "--version"])
                print("Chromium and Chromedriver installed successfully.")

            except subprocess.CalledProcessError as e:
                print(f"Failed to install Chromium or Chromedriver: {e}")
                sys.exit(1)

        # Check if Chromium is installed
        try:
            subprocess.check_call(["chromedriver", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Chromium and Chromedriver are already installed.")
        except FileNotFoundError:
            install_chromium()

    elif os_type == "Windows":
        # Instructions for Windows users
        def check_chromedriver():
            try:
                subprocess.check_call(["chromedriver", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print("Chromedriver is already installed on Windows.")
            except FileNotFoundError:
                print(
                    
                    "Chromedriver is not installed on Windows. Please download it manually from:\n"
                    "https://googlechromelabs.github.io/chrome-for-testing/"
                    ###
                    ### After navigating to chrome-for-testing, install platform chromedriver as needed, 
                    ### add the location of the unzipped file to PATH variable (i.e if it's stored in C:\Users\bob\Downloads\chromedriver-win64\chromedriver-win64 that will be the PATH variable)
                    ### Test success by running "chromedriver --version" in command prompt
                    ###
                )
                sys.exit(1)

        check_chromedriver()

    else:
        print(f"Unsupported OS: {os_type}. Please set up Chromium/Chromedriver manually.")
        sys.exit(1)

    # Install required Python packages - this is last because we want to ensure environment is ready for them
    print("Installing required Python packages...")
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} not found. Installing...")
            install_package(package)

    print("Environment setup complete.")

if __name__ == "__main__":
    setup_environment()