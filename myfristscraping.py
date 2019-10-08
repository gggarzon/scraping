from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll ("div",{"class":"item-container"})

filename = "funciono.csv"
f = open (filename,"w")

headers = "product name,shipping"

f.write(headers + "\n")
for container in containers:

    title_container = container.findAll("div",{"class":"item-info"})
    ahora = title_container[0].findAll("a",{"class":"item-title"})
    product = ahora[0].text

    shipping_container = container.findAll("div",{"class":"item-info"})
    ahora2 = title_container[0].findAll("li",{"class":"price-ship"})
    ship= ahora2[0].text.strip()


    print("product name: "+ product + "\n" )
    print ("shipping " + ship + "\n")
    
    f.write (product.replace(",","|") + ","+ ship + "\n")

f.close()