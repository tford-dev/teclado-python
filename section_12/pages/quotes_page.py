from selenium.webdriver.common.by import By
from locators.quotes_page_locator import QuotePageLocators;
from  parsers.quote import QuoteParser;

class QuotesPage:
    def __init__(self, browser):
        self.browser = browser;
    
    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, QuotePageLocators.QUOTE)];
        #return [QuoteParser(e) for e in self.browser.find_elements(QuotePageLocators.QUOTE)];