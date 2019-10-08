from tkinter import *
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.animeid.tv'



print ("ULTIMOS CAPITULOS ANIME by GERMAN \n")

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

ventana = Tk()
ventana.title ("ANIME")
ventana.config(bg="red")
miframe = Frame(ventana, width=1000, height=700,cursor="pirate")
miframe.config(bg="white")
miframe.pack()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll ("div",{"class":"main"})

j=0

item2 = containers[0].findAll ("div",{"class":"title"})

curs = Button(miframe,text="circle", relief=RAISED, cursor="circle")
curs.pack()
for i in range(0,len(item2)):
    contender = containers[0].findAll ("div",{"class":"dia"})
    contender2 = contender[i].findAll ("header")
    print("Fecha:" + item2[i].text.strip() + "\n")
    milabel2 = Label(miframe, text = "Fecha: "+ item2[i].text.strip()+"\n", fg="blue")
    milabel2.pack()
    j=0
    while j < len(contender2):
        print(contender2[j].text.strip()+ "\n" )
        milabel = Label(miframe, text =contender2[j].text.strip()+"\n")
        milabel.pack()
        j = j + 1
    
    


ventana.mainloop()