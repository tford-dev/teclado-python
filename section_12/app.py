from selenium import webdriver

from pages.quotes_page import QuotesPage;

chrome = webdriver.Chrome();
chrome.get('https://quotes.toscrape.com/search.aspx');
page = QuotesPage(chrome);

authors = page.get_authors() #list

#for some reason I could not get a method created that would do what the next 3 lines of code does
print("Your options for authors to browse quotes from are:")
for person in sorted(authors):
    print(person)
author = input("Enter the author you'd like to read quotes from: ")
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
selected_tag = input("Enter your tag for the kinds of quotes you'd like: ")

page.select_tag(selected_tag);
page.search_button.click();

print(page.quotes);