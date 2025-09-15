"""
Product Page class for MLM product page
"""
import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    """Product page object for MLM product"""
    
    # URLs
    GOLF_URL = "https://rapsodo.com/golf/"
    PRODUCTS_URL = "https://rapsodo.com/golf/products/"
    MLM_URL = "https://rapsodo.com/golf/mobile-launch-monitor/"
    
    # Locators
    PRODUCTS_BUTTON = (By.XPATH, "//a[contains(text(), 'Products')]")
    MLM_PRODUCT_LINK = (By.XPATH, "//a[contains(text(), 'MLM') or contains(text(), 'Mobile Launch Monitor')]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'ADD TO CART') or contains(text(), 'Add to Cart') or contains(text(), 'ADD TO CHART')]")
    PRODUCT_PRICE = (By.XPATH, "//*[contains(@class, 'price') or contains(@class, 'cost') or contains(@class, 'amount')]//*[contains(text(), '$')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.product_price = None
    
    def navigate_to_golf_section(self):
        """Navigate to golf section"""
        try:
            self.navigate_to(self.GOLF_URL)
            return True
        except Exception:
            return False
    
    def click_products_button(self):
        """Click on Products button"""
        products_selectors = [
            (By.XPATH, "//li[contains(@class, 'BoxedLink') and contains(text(), 'PRODUCTS')]"),
            (By.XPATH, "//div[contains(@class, 'Barlow') and contains(text(), 'PRODUCTS')]"),
            (By.XPATH, "//a[contains(text(), 'PRODUCTS')]"),
            (By.XPATH, "//button[contains(text(), 'PRODUCTS')]"),
            (By.XPATH, "//a[contains(text(), 'Products')]"),
            (By.XPATH, "//button[contains(text(), 'Products')]"),
            (By.XPATH, "//*[contains(text(), 'PRODUCTS') and (@role='button' or @role='link')]"),
            (By.XPATH, "//*[contains(text(), 'Products') and (@role='button' or @role='link')]"),
            (By.XPATH, "//nav//a[contains(text(), 'Products')]"),
            (By.CSS_SELECTOR, "a[href*='products']"),
            (By.CSS_SELECTOR, "button[href*='products']"),
            (By.CSS_SELECTOR, ".BoxedLink[contains(text(), 'PRODUCTS')]"),
            (By.XPATH, "//*[contains(@class, 'OpenMenu') and contains(text(), 'PRODUCTS')]")
        ]
        
        for selector in products_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(3)
                    return True
            except Exception:
                continue
        
        # If no specific Products button found, continue (maybe already on products page)
        print("⚠ No Products button found, continuing...")
        return True
    
    def click_mlm_product(self):
        """Click on MLM product - specifically SHOP MLM button"""
        mlm_selectors = [
            (By.XPATH, "//a[contains(text(), 'SHOP MLM')]"),
            (By.XPATH, "//a[contains(text(), 'Shop MLM')]"),
            (By.XPATH, "//a[contains(text(), 'SHOP NOW') and contains(@href, 'mobile-launch-monitor')]"),
            (By.XPATH, "//a[contains(@href, 'products/mobile-launch-monitor')]"),
            (By.CSS_SELECTOR, "a[href*='products/mobile-launch-monitor']"),
            (By.XPATH, "//a[@class='hero-slider-button' and contains(@href, 'mobile-launch-monitor')]"),
            (By.XPATH, "//a[contains(text(), 'Choose MLM')]"),
            (By.XPATH, "//button[contains(text(), 'Choose MLM')]"),
            (By.XPATH, "//a[contains(text(), 'MLM') and contains(@href, 'products')]"),
            (By.XPATH, "//button[contains(text(), 'MLM')]")
        ]
        
        for selector in mlm_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(3)
                    return True
            except Exception:
                continue
        
        return False
    
    def verify_mlm_page_title(self):
        """Verify that we're on the MLM page by checking title"""
        page_title = self.get_page_title()
        return "Mobile Launch Monitor" in page_title or "MLM" in page_title
    
    def select_mlm_option(self):
        """Select MOBILE LAUNCH MONITOR option from the right side"""
        mlm_option_selectors = [
            (By.XPATH, "//*[contains(text(), 'MOBILE LAUNCH MONITOR') or contains(text(), 'Mobile Launch Monitor')]"),
            (By.XPATH, "//button[contains(text(), 'MOBILE LAUNCH MONITOR')]"),
            (By.XPATH, "//a[contains(text(), 'MOBILE LAUNCH MONITOR')]")
        ]
        
        for selector in mlm_option_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(3)
                    return True
            except Exception:
                continue
        return False
    
    def get_product_price(self):
        """Get the product price"""
        price_selectors = [
            (By.XPATH, "//*[contains(@class, 'price')]//*[contains(text(), '$')]"),
            (By.XPATH, "//*[contains(@class, 'cost')]//*[contains(text(), '$')]"),
            (By.XPATH, "//*[contains(@class, 'amount')]//*[contains(text(), '$')]"),
            (By.XPATH, "//*[contains(text(), '$')]"),
            (By.XPATH, "//span[contains(text(), '$')]"),
            (By.XPATH, "//div[contains(text(), '$')]")
        ]
        
        for selector in price_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.product_price = self.get_text(selector)
                    return self.product_price
            except Exception:
                continue
        return None
    
    def click_add_to_cart(self):
        """Click ADD TO CART button"""
        add_to_cart_selectors = [
            (By.XPATH, "//button[contains(text(), 'ADD TO CART')]"),
            (By.XPATH, "//button[contains(text(), 'Add to Cart')]"),
            (By.XPATH, "//button[contains(text(), 'ADD TO CHART')]"),
            (By.XPATH, "//a[contains(text(), 'ADD TO CART')]"),
            (By.XPATH, "//input[@value='Add to Cart']"),
            (By.XPATH, "//button[contains(@class, 'add-to-cart')]"),
            (By.XPATH, "//button[contains(@class, 'btn-add-cart')]"),
            (By.XPATH, "//*[contains(text(), 'Add to Cart') and (@role='button' or @type='submit')]"),
            (By.XPATH, "//button[contains(text(), 'Buy')]"),
            (By.XPATH, "//button[contains(text(), 'Purchase')]"),
            (By.XPATH, "//button[contains(text(), 'Shop')]")
        ]
        
        for selector in add_to_cart_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(3)
                    return True
            except Exception:
                continue
        return False
    
    def verify_redirected_to_cart(self):
        """Verify that user is redirected to cart screen"""
        current_url = self.get_current_url()
        cart_indicators = ["cart", "checkout", "basket"]
        return any(indicator in current_url.lower() for indicator in cart_indicators)
