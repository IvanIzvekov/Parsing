import requests
from bs4 import BeautifulSoup
from tkinter import *  
from tkinter.ttk import Combobox

page = requests.get('https://coinmarketcap.com')
soup = BeautifulSoup(page.text, 'html.parser')
name = soup.find("table").find_all(class_="sc-1eb5slv-0 iworPT")
price = soup.find("table").find_all(class_="sc-131di3y-0 cLgOOr")
world_cap = soup.find("table").find_all(class_="sc-1ow4cwt-1 ieFnWP")

counter=0
while counter<10:
	print(name[counter].text, price[counter].text, world_cap[counter].text)
	counter=counter+1
counter=0

window = Tk()
window.title("IP-017 Izvekov Ivan")
window.geometry('300x150')
combo = Combobox(window)
input_text = Label(window, text = "Name:", fg = "grey")
price_text = Label(window, text = "Price:", fg = "grey")
worldcup_text = Label(window, text = "Global capitalization:", fg = "grey")
price_output = Entry(window,width=20, state='readonly')
worldcup_output = Entry(window,width=20, state='readonly')

input_text.grid(column = 0, row = 0)
price_text.grid(column = 1, row = 0)
worldcup_text.grid(column = 1, row = 2)
price_output.grid(column = 1, row = 1)
worldcup_output.grid(column = 1, row = 3)
combo['values'] = (name[0].text, name[1].text, name[2].text, name[3].text, name[4].text, name[5].text, name[6].text, name[7].text, name[8].text, name[9].text)
combo.current(0)
combo.grid(column=0, row=1)

while counter<10:
	if combo.get() == name[counter].text:
		price_output.insert(0, text = price[combo.current()].text)
		worldcup_output.insert(0, text = world_cap[combo.current()].text)
	counter = counter + 1

window.mainloop()