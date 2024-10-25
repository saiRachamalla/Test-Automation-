class JavatpointPage:
    
    def __init__(self, page):
        self.page = page
    
    def open(self):
        self.page.goto("https://www.javatpoint.com/")
    
    def wait_for_page(self):
        self.page.wait_for_timeout(5000)

    def page_actions(self):
        self.page.get_by_role("link", name="Tutorials").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("link", name="Interview").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("button", name="Compiler").click()
        self.page.wait_for_timeout(3000)
    
    def close(self):
        self.page.close()
