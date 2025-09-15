"""
Driver Manager for WebDriver setup with automatic ChromeDriver management.
Includes fallback mechanisms and platform-specific optimizations.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


class DriverManager:
    """Manages WebDriver setup with factory pattern and error handling fallbacks."""
    
    @staticmethod
    def get_chrome_driver():
        """Setup Chrome WebDriver with optimized configuration and fallback mechanisms."""
        options = webdriver.ChromeOptions()
        
        # Basic options for automation
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        
        # macOS Chrome binary path
        if os.path.exists("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
            options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        
        # Hide automation indicators
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        try:
            # Try WebDriverManager first
            driver_path = ChromeDriverManager().install()
            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=options)
            print("✓ ChromeDriver setup successful with WebDriverManager")
        except Exception as e:
            print(f"ChromeDriverManager failed: {e}")
            try:
                # Fallback to system ChromeDriver
                driver = webdriver.Chrome(options=options)
                print("✓ ChromeDriver setup successful with system driver")
            except Exception as e2:
                print(f"System ChromeDriver failed: {e2}")
                # Final fallback
                driver = webdriver.Chrome(options=options)
                print("✓ ChromeDriver setup successful (fallback)")
        
        # Hide webdriver property for bot detection bypass
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver
    
    @staticmethod
    def quit_driver(driver):
        """Terminate WebDriver and clean up resources."""
        if driver:
            driver.quit()
