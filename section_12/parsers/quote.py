from selenium.webdriver.common.by import By
from locators.quotes_locators import QuoteLocators;

class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote(quote content, author, tags)
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Quote: {self.content}, by {self.author}>"

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        elements = self.parent.find_element(By.CSS_SELECTOR, locator)
        return elements.text;
    
    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        element = self.parent.find_element(By.CSS_SELECTOR, locator)
        return element.text
    
    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        #return [e.string for e in self.parent.find_elements_by_css_selector(locator)];
        elements = self.parent.find_elements(By.CSS_SELECTOR, locator)
        return [element.text for element in elements]