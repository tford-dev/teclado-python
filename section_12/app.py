from selenium import webdriver

from pages.quotes_page import QuotesPage;

chrome = webdriver.Chrome();
chrome.get('https://quotes.toscrape.com');
page = QuotesPage(chrome);


for quote in page.quotes:
    print(quote);