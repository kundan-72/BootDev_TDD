from xml.etree.ElementTree import TreeBuilder
from lxml import html

# Use the html.fromstring method to get a document tree.
# Use the tree's make_links_absolute method to convert all the links in the tree to absolute URLs.
# Use the tree's iter() method, for elem in tree.iter(): to iterate over each HTML tag.
# If an element is a link, which you can check by making sure it's
# .tag property is "a", append the URL to a list that you'll return 
# at the end of the function. You can get the URL from the 
# element using the .get() method: elem.get("href").

def get_urls_from_string(page_content, base_url):
    tree = html.fromstring(page_content)
    tree.make_links_absolute(base_url)
    urls = []
    for elem in abs.iter():
        if elem.tag == "a":
            url = elem.get("href")
            urls.append(url) 