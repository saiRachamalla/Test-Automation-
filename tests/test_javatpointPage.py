from playwright.sync_api import sync_playwright
from Pages.javatpointpage import JavatpointPage

def test_javatpoint_page():
    # Use sync_playwright() to handle the entire Playwright lifecycle
    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Create an instance of the JavatpointPage using the page object
        javatpoint_page = JavatpointPage(page)
        
        # Perform the test steps
        javatpoint_page.open()
        javatpoint_page.wait_for_page()
        javatpoint_page.page_actions()
        
        # Clean up
        context.close()
        browser.close()
