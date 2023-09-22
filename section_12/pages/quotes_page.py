from typing import List
from selenium.common.exceptions import NoSuchElementException;
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from locators.quotes_page_locator import QuotePageLocators;
from  parsers.quote import QuoteParser;

class QuotesPage:
    def __init__(self, browser):
        self.browser = browser;
    
    @property
    def quotes(self) -> List[QuoteParser]:
        return [QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, QuotePageLocators.QUOTE)];
        #return [QuoteParser(e) for e in self.browser.find_elements(QuotePageLocators.QUOTE)];

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.AUTHOR_DROPDOWN)
        return Select(element);

    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.TAG_DROPDOWN)
        return Select(element);

    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.SEARCH_BUTTON)
    
    def get_authors(self):
        return [option.text.strip() for option in self.author_dropdown.options]

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name);

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]
    
    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)

    # def search_for_quotes(self, author_name: str, tag_name: str) -> List[QuoteParser]:
    #     self.select_author(author_name)
    #     tags = self.get_available_tags()
    #     print("Select one of these tags: [{}]".format(" | ".join(tags)))
    #     try:
    #         self.select_tag(tag_name);
    #     except NoSuchElementException: 
    #         raise InvalidTagForAuthorError(
    #             f"Author '{author_name}' does not have any data tagged with '{tag_name}'."
    #         )
    #     self.search_button.click()
    #     return self.quotes
    
    def search_for_quotes(self) -> List[QuoteParser]:
        author_name = input("Enter the author you'd like to read quotes from: ")
        self.select_author(author_name)
        tags = self.get_available_tags()
        print("Select one of these tags: [{}]".format(" | ".join(tags)))
        tag_name = input(
            "Enter your tag for the kinds of quotes you'd like: ")
        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author_name}' does not have any data tagged with '{tag_name}'."
            )
        self.search_button.click()
        return self.quotes

#Placeholder 
class InvalidTagForAuthorError(ValueError):
    pass;