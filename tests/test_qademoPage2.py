from playwright.sync_api import sync_playwright
from Pages.qademopage2 import QaDemo2

def test_javatpoint_page():
    
    with sync_playwright() as playwright:
        
        # Launch the browser
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Create an instance of the QaDemo2 class
        qademo_page = QaDemo2(page)
        
        # Perform the test steps
        qademo_page.open()
        qademo_page.click_elements()
        qademo_page.fill_user_details_from_excel()
        
        # Clean up
        context.close()
        browser.close()