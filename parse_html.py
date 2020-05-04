from bs4.element import NavigableString
from bs4.element import Tag
from bs4 import BeautifulSoup as bs


# Open a file: file
file_name = "downloads/rightwingstudysquad.html"
file = open(file_name,mode='r')
 
# read all lines at once
html_doc = file.read()
 
# close the file
file.close()


soup = bs(html_doc, 'html.parser')

list_items = soup.find_all('li')

x = 0

followers = {}

for item in list_items:
  follower = {}
  for child in item.descendants:
    # print("CHILD")
    # print(type(child))
    # print(child)
    if type(child) == Tag:
      # print(child.name)
      if child.name == 'img':
        follower['profile_picture'] = child.attrs['src']
      elif child.name == 'a':
        if child.attrs['class'][0] == 'FPmhX':
          # print("USErNAME")
          follower['username'] = str(child.contents[0]).strip()
      elif child.name == 'div' and child.attrs['class'][0] == 'wFPL8':
        # print("FULL NAME")
        # print(str(child.contents[0]))
        follower['full_name'] = str(child.contents[0]).strip()

  if 'username' in follower:
    followers[follower['username']] = follower

print(len(followers))
