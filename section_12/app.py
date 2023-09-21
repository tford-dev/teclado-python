from selenium import webdriver

from pages.quotes_page import QuotesPage;

chrome = webdriver.Chrome();
chrome.get('https://quotes.toscrape.com/search.aspx');
page = QuotesPage(chrome);

author = input("Enter the author you'd like to read quotes from: ")
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
selected_tag = input("Enter your tag for the kinds of quotes you'd like: ")

page.select_tag(selected_tag);
page.search_button.click();

print(page.quotes);