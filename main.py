# This script will accept an url and a tag
# and return the innerText of the first occurrence of that tag.

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Get the url and tag from the command line
# url = sys.argv[1]
# tag = sys.argv[2]
url = "https://www.goodreads.com/book/show/53291522.here"
tag = "h1"
first_tag = "Tag not found"

# Open the url and read the html
html = urlopen(url).read()

# Convert the html to a BeautifulSoup object
soup = BeautifulSoup(html, "lxml")

if tag == "h1":
    # loop through all heading tags (h1-h6) and find the first one
    for i in range(1, 7):
        h = soup.find('h' + str(i))
        if h:
            first_tag = h.get_text().strip()
            break
else:
    # find the first occurrence of the tag
    first_tag = soup.find(tag).get_text().strip()


print(first_tag)
