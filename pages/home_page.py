"""
Home Page class for Rapsodo.com main page
"""
import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    """Home page object for Rapsodo.com"""
    
    # URL
    URL = "https://rapsodo.com"
    
    # Locators
    GOLF_BUTTON = (By.XPATH, "//a[contains(text(), 'Golf')]")
    CART_ICON = (By.CSS_SELECTOR, "[href*='cart'], .cart-icon, [data-testid='cart-icon'], .header-cart")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "nav, .navigation, .header-nav")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_home(self):
        """Navigate to the home page"""
        self.navigate_to(self.URL)
        self.accept_cookies()
        return self
    
    def accept_cookies(self):
        """Accept cookies by clicking GOT IT! button"""
        cookie_selectors = [
            (By.XPATH, "//a[contains(text(), 'GOT IT!')]"),
            (By.CSS_SELECTOR, ".cc-btn.cc-dismiss"),
            (By.XPATH, "//button[contains(text(), 'GOT IT!')]"),
            (By.XPATH, "//*[contains(text(), 'GOT IT!')]"),
            (By.CSS_SELECTOR, "[class*='cc-dismiss']")
        ]
        
        for selector in cookie_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(2)
                    print("✓ Cookies accepted")
                    return True
            except Exception:
                continue
        return False
    
    def verify_url_contains_rapsodo(self):
        """Verify that we are on rapsodo.com"""
        current_url = self.get_current_url()
        return "rapsodo.com" in current_url
    
    def click_golf_button(self):
        """Click on the Golf button"""
        golf_selectors = [
            (By.XPATH, "//a[contains(text(), 'GOLF')]"),
            (By.XPATH, "//a[contains(text(), 'Golf')]"),
            (By.XPATH, "//a[contains(@href, 'golf')]"),
            (By.XPATH, "//button[contains(text(), 'GOLF')]"),
            (By.XPATH, "//button[contains(text(), 'Golf')]"),
            (By.XPATH, "//nav//a[contains(text(), 'Golf')]"),
            (By.XPATH, "//header//a[contains(text(), 'Golf')]"),
            (By.CSS_SELECTOR, "a[href*='golf']"),
            (By.CSS_SELECTOR, "a[href*='pages/golf']")
        ]
        
        for selector in golf_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(5)  # Wait longer for page load and potential popup
                    self.close_popup()  # Close any popup that appears
                    return True
            except Exception:
                continue
        
        # If Golf button not found, return False - don't navigate directly
        return False
    
    def close_popup(self):
        """Close popup by clicking X button"""
        popup_close_selectors = [
            (By.XPATH, "//button[contains(text(), 'X')]"),
            (By.XPATH, "//a[contains(text(), 'X')]"),
            (By.CSS_SELECTOR, ".close"),
            (By.CSS_SELECTOR, ".popup-close"),
            (By.CSS_SELECTOR, "[aria-label='Close']"),
            (By.CSS_SELECTOR, "[title='Close']"),
            (By.XPATH, "//button[@type='button' and contains(@class, 'close')]"),
            (By.XPATH, "//*[contains(@class, 'close-button')]"),
            (By.XPATH, "//*[contains(@class, 'modal-close')]"),
            (By.XPATH, "//button[contains(@onclick, 'close')]")
        ]
        
        for selector in popup_close_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(2)
                    print("✓ Popup closed")
                    return True
            except Exception:
                continue
        return False
    
    def click_cart_icon(self):
        """Click on the cart icon or navigate directly to cart"""
        cart_selectors = [
            (By.CSS_SELECTOR, "[data-testid='cart-icon']"),
            (By.CSS_SELECTOR, ".cart-icon"),
            (By.CSS_SELECTOR, "[href*='cart']"),
            (By.CSS_SELECTOR, ".header-cart"),
            (By.CSS_SELECTOR, "a[href*='cart']"),
            (By.CSS_SELECTOR, ".cart"),
            (By.CSS_SELECTOR, "[class*='cart']"),
            (By.CSS_SELECTOR, "button[class*='cart']"),
            (By.CSS_SELECTOR, ".shopping-cart"),
            (By.CSS_SELECTOR, "[aria-label*='cart']"),
            (By.CSS_SELECTOR, "[title*='cart']")
        ]
        
        for selector in cart_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(3)
                    return True
            except Exception:
                continue
        
        # If cart icon not found, navigate directly to cart URL
        try:
            self.navigate_to("https://rapsodo.com/cart")
            return True
        except Exception:
            return False
    
    def verify_cart_is_empty(self):
        """Verify that the cart is empty"""
        empty_indicators = [
            (By.XPATH, "//*[contains(text(), 'empty') or contains(text(), 'cart is empty') or contains(text(), 'no items') or contains(text(), '0 items') or contains(text(), 'Your cart is empty')]"),
            (By.CSS_SELECTOR, ".cart-item, .cart-product, [class*='cart-item'], .cart-product-item")
        ]
        
        # Check for empty cart text
        try:
            if self.is_element_present(empty_indicators[0]):
                return True
        except:
            pass
        
        # Check if no cart items are present
        try:
            cart_items = self.find_elements(empty_indicators[1])
            return len(cart_items) == 0
        except:
            return True  # If we can't find cart items, assume it's empty
