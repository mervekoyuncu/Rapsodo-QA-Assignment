"""
Base Page class containing common functionality for all pages.
Implements POM pattern with reusable web element interaction methods.
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Base class for all page objects with common web element interactions."""
    
    def __init__(self, driver):
        """Initialize with WebDriver instance and 10-second default wait."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to(self, url):
        """Navigate to URL with 2-second page load wait."""
        self.driver.get(url)
        time.sleep(2)
    
    def wait_for_element(self, locator, timeout=10):
        """Wait for element to be present in DOM."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_clickable(self, locator, timeout=10):
        """Wait for element to be clickable (visible and enabled)."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def click_element(self, locator):
        """Click element using multiple strategies: standard click, JavaScript click, scroll+click."""
        strategies = [
            lambda: self.wait_for_clickable(locator).click(),
            lambda: self.driver.execute_script("arguments[0].click();", self.find_element(locator)),
            lambda: self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", self.find_element(locator))
        ]
        
        for strategy in strategies:
            try:
                strategy()
                return True
            except Exception:
                continue
        return False
    
    def find_element(self, locator):
        """Find a single element using the provided locator."""
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """Find multiple elements using the provided locator."""
        return self.driver.find_elements(*locator)
    
    def get_text(self, locator):
        """Extract text content from an element."""
        return self.find_element(locator).text
    
    def is_element_present(self, locator):
        """Check if element exists in DOM (no waiting)."""
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False
    
    def is_element_displayed(self, locator):
        """Check if element is present and visible."""
        try:
            return self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False
    
    def scroll_to_element(self, locator):
        """Scroll to bring element into viewport with 1-second wait."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
    
    def get_current_url(self):
        """Get current browser URL."""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get current page title."""
        return self.driver.title
    
    def wait_for_url_contains(self, text, timeout=10):
        """Wait for URL to contain specific text."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(text))
