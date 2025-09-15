"""
Cart Page class for cart functionality
"""
import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Cart page object"""
    
    # Locators
    QUANTITY_INCREASE_BUTTON = (By.XPATH, "//button[contains(@class, 'increase') or contains(@class, 'plus') or text()='+']")
    QUANTITY_INPUT = (By.XPATH, "//input[@type='number' or contains(@class, 'quantity')]")
    QUANTITY_DISPLAY = (By.XPATH, "//*[contains(@class, 'quantity') or contains(@class, 'count')]//*[text()='2']")
    TOTAL_PRICE = (By.XPATH, "//*[contains(text(), '$') and (contains(@class, 'total') or contains(@class, 'subtotal') or contains(@class, 'price'))]")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item, .cart-product, [class*='cart-item'], .cart-product-item")
    PRODUCT_PRICE_IN_CART = (By.XPATH, "//*[contains(@class, 'price') or contains(@class, 'cost') or contains(@class, 'amount')]//*[contains(text(), '$')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_cart(self):
        """Navigate to cart by clicking cart icon or direct URL"""
        cart_selectors = [
            (By.CSS_SELECTOR, "[data-testid='cart-icon']"),
            (By.CSS_SELECTOR, ".cart-icon"),
            (By.CSS_SELECTOR, "[href*='cart']"),
            (By.CSS_SELECTOR, ".header-cart"),
            (By.CSS_SELECTOR, "a[href*='cart']"),
            (By.CSS_SELECTOR, ".cart"),
            (By.CSS_SELECTOR, "[class*='cart']"),
            (By.CSS_SELECTOR, "button[class*='cart']"),
            (By.CSS_SELECTOR, ".shopping-cart")
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
    
    def increase_quantity_to_two(self):
        """Increase quantity to 2"""
        # Strategy 1: Find and click quantity increase button
        quantity_increase_selectors = [
            (By.XPATH, "//button[contains(@class, 'increase')]"),
            (By.XPATH, "//button[contains(@class, 'plus')]"),
            (By.XPATH, "//button[text()='+']"),
            (By.XPATH, "//button[contains(@aria-label, 'increase')]"),
            (By.XPATH, "//button[contains(@aria-label, 'plus')]"),
            (By.XPATH, "//*[contains(@class, 'qty-increase')]"),
            (By.XPATH, "//*[contains(@class, 'quantity-increase')]"),
            (By.XPATH, "//button[@type='button' and contains(@onclick, 'increase')]")
        ]
        
        for selector in quantity_increase_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(2)
                    return True
            except Exception:
                continue
        
        # Strategy 2: If increase button not found, try to modify quantity input field
        quantity_input_selectors = [
            (By.XPATH, "//input[@type='number']"),
            (By.XPATH, "//input[contains(@class, 'quantity')]"),
            (By.XPATH, "//input[contains(@name, 'quantity')]"),
            (By.XPATH, "//input[contains(@id, 'quantity')]"),
            (By.XPATH, "//input[@min='1']"),
            (By.XPATH, "//select[contains(@class, 'quantity')]")
        ]
        
        for selector in quantity_input_selectors:
            try:
                if self.is_element_displayed(selector):
                    quantity_input = self.find_element(selector)
                    # Clear and set quantity to 2
                    self.driver.execute_script("arguments[0].value = '';", quantity_input)
                    quantity_input.send_keys("2")
                    # Trigger change event
                    self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", quantity_input)
                    time.sleep(2)
                    return True
            except Exception:
                continue
        
        return False
    
    def decrease_quantity_to_one(self):
        """Decrease quantity from 2 to 1"""
        # Strategy 1: Find and click quantity decrease button
        quantity_decrease_selectors = [
            (By.XPATH, "//button[contains(@class, 'decrease')]"),
            (By.XPATH, "//button[contains(@class, 'minus')]"),
            (By.XPATH, "//button[text()='-']"),
            (By.XPATH, "//button[contains(@aria-label, 'decrease')]"),
            (By.XPATH, "//button[contains(@aria-label, 'minus')]"),
            (By.XPATH, "//*[contains(@class, 'qty-decrease')]"),
            (By.XPATH, "//*[contains(@class, 'quantity-decrease')]"),
            (By.XPATH, "//button[@type='button' and contains(@onclick, 'decrease')]")
        ]
        
        for selector in quantity_decrease_selectors:
            try:
                if self.is_element_displayed(selector):
                    self.click_element(selector)
                    time.sleep(2)
                    return True
            except Exception:
                continue
        
        # Strategy 2: If decrease button not found, try to modify quantity input field
        quantity_input_selectors = [
            (By.XPATH, "//input[@type='number']"),
            (By.XPATH, "//input[contains(@class, 'quantity')]"),
            (By.XPATH, "//input[contains(@name, 'quantity')]"),
            (By.XPATH, "//input[contains(@id, 'quantity')]"),
            (By.XPATH, "//input[@min='1']"),
            (By.XPATH, "//select[contains(@class, 'quantity')]")
        ]
        
        for selector in quantity_input_selectors:
            try:
                if self.is_element_displayed(selector):
                    quantity_input = self.find_element(selector)
                    # Clear and set quantity to 1
                    self.driver.execute_script("arguments[0].value = '';", quantity_input)
                    quantity_input.send_keys("1")
                    # Trigger change event
                    self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", quantity_input)
                    time.sleep(2)
                    return True
            except Exception:
                continue
        
        return False
    
    def verify_quantity_is_two(self):
        """Verify that quantity is set to 2"""
        quantity_verification_selectors = [
            (By.XPATH, "//*[contains(@class, 'quantity')]//*[text()='2']"),
            (By.XPATH, "//*[contains(@class, 'count')]//*[text()='2']"),
            (By.XPATH, "//input[@value='2']"),
            (By.XPATH, "//*[contains(@class, 'qty')]//*[text()='2']"),
            (By.XPATH, "//*[contains(text(), 'Qty: 2')]"),
            (By.XPATH, "//*[contains(text(), 'Quantity: 2')]")
        ]
        
        for selector in quantity_verification_selectors:
            try:
                if self.is_element_displayed(selector):
                    return True
            except Exception:
                continue
        return False
    
    def verify_quantity_is_one(self):
        """Verify that quantity is set to 1"""
        quantity_verification_selectors = [
            (By.XPATH, "//*[contains(@class, 'quantity')]//*[text()='1']"),
            (By.XPATH, "//*[contains(@class, 'count')]//*[text()='1']"),
            (By.XPATH, "//input[@value='1']"),
            (By.XPATH, "//*[contains(@class, 'qty')]//*[text()='1']"),
            (By.XPATH, "//*[contains(text(), 'Qty: 1')]"),
            (By.XPATH, "//*[contains(text(), 'Quantity: 1')]")
        ]
        
        for selector in quantity_verification_selectors:
            try:
                if self.is_element_displayed(selector):
                    return True
            except Exception:
                continue
        return False
    
    def get_total_cost(self):
        """Get the total cost"""
        total_selectors = [
            (By.XPATH, "//*[contains(text(), '$') and contains(@class, 'total')]"),
            (By.XPATH, "//*[contains(text(), '$') and contains(@class, 'subtotal')]"),
            (By.XPATH, "//*[contains(text(), '$') and contains(@class, 'price')]"),
            (By.XPATH, "//*[contains(text(), '$') and contains(@class, 'amount')]"),
            (By.XPATH, "//*[contains(text(), '$') and contains(@class, 'cost')]"),
            (By.XPATH, "//*[contains(text(), 'Total')]//*[contains(text(), '$')]"),
            (By.XPATH, "//*[contains(text(), 'Subtotal')]//*[contains(text(), '$')]")
        ]
        
        for selector in total_selectors:
            try:
                if self.is_element_displayed(selector):
                    return self.get_text(selector)
            except Exception:
                continue
        return None
    
    def verify_price_matches(self, original_price):
        """Verify that the price in cart matches the original price"""
        if not original_price:
            return False
        
        cart_price_selectors = [
            (By.XPATH, "//*[contains(@class, 'price')]//*[contains(text(), '$')]"),
            (By.XPATH, "//*[contains(@class, 'cost')]//*[contains(text(), '$')]"),
            (By.XPATH, "//*[contains(@class, 'amount')]//*[contains(text(), '$')]"),
            (By.XPATH, "//*[contains(text(), '$')]")
        ]
        
        for selector in cart_price_selectors:
            try:
                if self.is_element_displayed(selector):
                    cart_price = self.get_text(selector)
                    # Check if prices match (allowing for slight differences in formatting)
                    if any(price_part in cart_price for price_part in original_price.split()) or any(price_part in original_price for price_part in cart_price.split()):
                        return True
            except Exception:
                continue
        return False
    
    def verify_two_items_in_cart(self):
        """Verify that there are 2 items in the cart"""
        try:
            cart_items = self.find_elements(self.CART_ITEMS)
            return len(cart_items) == 2
        except Exception:
            return False
