#! /usr/bin/python

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://inventwithpython.com/')

# finding elements
# try:
#     elems = browser.find_elements_by_class_name('cover-thumb')
#     for elem in elems:
#         print('found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('was not able to find an element with that class name')

# Clicking links
# linkElem = browser.find_element_by_link_text('Python Pocket Reference')
# linkElem.click()

# use WebElement.send_keys() to send keystrokes
# use Keys object for special keys such as arrow keys, page_up, etc
# use WebElement.submit() to submit form
# use browser.back(), etc for browser navigation buttons
