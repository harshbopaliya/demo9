import requests
from bs4 import BeautifulSoup

with open('sample.html',"r") as f: 
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
#print(soup.prettify())
#print(soup.title.string,type(soup.title.string))
#print(soup.find_all('div')[0])

# for link in soup.find_all("a"):
#     print(link.get('href'))
#     print(link.get_text())

# s =soup.find(id="link3")
# print(s.get('href'))

# print(s.get_text())

# print(soup.select("div.italic"))
# print(soup.select("span#italic"))

# print(soup.span.get("class"))
#print(soup.find(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)


# i=0

# for parent in soup.find(class_="box").parents:
#     i+=1
#     print(parent)
#     if (i==2):
#         break

# count = soup.find(class_="container")
# count.name="span"
# count["class"] = "myclass class2"
# count.string="I am string"
# print(count)

# ulTag = soup.new_tag("ul")
# liTag = soup.new_tag("li")
# liTag.string= "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string= "about"
# ulTag.append(liTag)


# soup.html.body.insert(0,ulTag)
# with open("modified.html","w") as f:
#     f.write(str(soup))

# cont = soup.find(class_="container")
# print(cont.has_attr("contenteditable"))


def has_class_but_not_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

#results = soup.find_all(has_class_but_not_id)

results = soup.find_all(has_content)
for result in results:
    print(result,"\n\n")