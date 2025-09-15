# Rapsodo.com Cart Automation Test - Page Object Model

This project implements automated testing for Rapsodo.com cart functionality using Selenium WebDriver with the Page Object Model (POM) design pattern.

## Project Structure

```
rapsodo_test/
├── pages/                    # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py         # Base page with common functionality
│   ├── home_page.py         # Home page object
│   ├── product_page.py      # Product page object
│   └── cart_page.py         # Cart page object
├── tests/                   # Test files
│   ├── __init__.py
│   └── test_rapsodo_cart.py # Main test file
├── utils/                   # Utility classes
│   ├── __init__.py
│   └── driver_manager.py    # WebDriver management
├── conftest.py             # Pytest configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── TEST_REPORT.md         # Detailed test execution report
```

## Test Cases Implemented

1. **Navigation Test**: Navigate to rapsodo.com and verify the URL
2. **Empty Cart Verification**: Click cart icon and verify cart is empty
3. **Product Selection**: Navigate to Golf > Products > Mobile Launch Monitor (MLM)
4. **Add to Cart**: Add MLM product to cart and verify redirection
5. **Quantity Management**: Increase quantity to 2 and verify total cost
6. **Quantity Decrease**: Decrease quantity from 2 to 1 and verify updated total

## Features

- **Page Object Model**: Clean separation of page elements and test logic
- **Robust Element Finding**: Multiple selector strategies for reliable element detection
- **ChromeDriver Management**: Automatic driver setup with fallback mechanisms
- **Error Handling**: Comprehensive exception handling and logging
- **Cross-Platform**: Works on macOS with automatic Chrome binary detection

## Requirements

- Python 3.7+
- Chrome browser installed
- Internet connection

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tests

### Option 1: Run the main test file directly
```bash
python tests/test_rapsodo_cart.py
```

### Option 2: Run with pytest
```bash
pytest tests/test_rapsodo_cart.py -v
```

### Option 3: Run specific test cases
```bash
pytest tests/test_rapsodo_cart.py::TestRapsodoCart::test_case_1_navigate_to_rapsodo -v
```

## Page Object Model Benefits

1. **Maintainability**: Page elements are centralized and easy to update
2. **Reusability**: Page objects can be reused across multiple tests
3. **Readability**: Tests are more readable and business-focused
4. **Scalability**: Easy to add new pages and functionality
5. **Separation of Concerns**: Test logic separated from page implementation

## ChromeDriver Setup

The project includes automatic ChromeDriver management:
- Uses WebDriverManager to automatically download and manage ChromeDriver
- Falls back to system ChromeDriver if WebDriverManager fails
- Automatically detects Chrome binary location on macOS
- Includes browser optimization settings for automation

## Test Output

The tests provide detailed output showing:
- ✓ Successful operations
- ⚠ Warnings for non-critical issues
- ❌ Failures with detailed error messages
- Progress indicators for each test case

## Error Handling

The framework includes robust error handling:
- Multiple selector strategies for element finding
- Graceful fallbacks when primary methods fail
- Detailed logging for debugging
- Automatic cleanup of browser resources

## Customization

To extend the framework:
1. Add new page objects in the `pages/` directory
2. Create new test methods in `test_rapsodo_cart.py`
3. Add utility functions in the `utils/` directory
4. Configure additional fixtures in `conftest.py`
