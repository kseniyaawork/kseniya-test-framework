import xml.etree.ElementTree as ET

tree = ET.parse('library.xml')
root = tree.getroot()


for book in root.findall("book"):
    our_book = book.find(["Ralls, Kim"]).text
    title = book.find("title").text
    genre = book.find("genre").text

    print(our_book)




