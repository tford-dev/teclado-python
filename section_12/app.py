from selenium import webdriver

from pages.quotes_page import QuotesPage;

chrome = webdriver.Chrome();
chrome.get('https://quotes.toscrape.com/search.aspx');
page = QuotesPage(chrome);

#for some reason I could not get a method created that would do what the next 4 lines of code does
authors = page.get_authors()  # list
print("Your options for authors to browse quotes from are:")
for person in sorted(authors):
    print(person)

print(page.search_for_quotes())
