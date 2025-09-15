"""
Pytest configuration file
"""
import pytest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="session")
def driver():
    """Fixture to provide WebDriver instance"""
    from utils.driver_manager import DriverManager
    driver = DriverManager.get_chrome_driver()
    yield driver
    DriverManager.quit_driver(driver)


@pytest.fixture(scope="session")
def pages(driver):
    """Fixture to provide page objects"""
    from pages.home_page import HomePage
    from pages.product_page import ProductPage
    from pages.cart_page import CartPage
    
    return {
        'home': HomePage(driver),
        'product': ProductPage(driver),
        'cart': CartPage(driver)
    }
