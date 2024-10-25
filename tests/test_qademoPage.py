from playwright.sync_api import sync_playwright
from Pages.qademoPage import QaDemo

def test_qademo_page1():
    # Use sync_playwright() to handle the entire Playwright lifecycle
    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Create an instance of the JavatpointPage using the page object
        qademo_page = QaDemo(page)
        
        # Perform the test steps
        qademo_page.open()
        # qademo_page.click_elements()
        # qademo_page.fill_user_details_from_excel()
        qademo_page.click_practice()
        qademo_page.fill_practice_form()
        
        # Clean up
        context.close()
        browser.close()
