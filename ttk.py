#!/usr/bin/env pyhon3.9

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import csv

filepath = './test.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])
print(Data)

root = ThemedTk(theme='radiance')

root.title('Action Figure Collection 2021')
root.geometry("1000x1000")

ttk.Label(root,
                    text="Ralph's Action Figure Collection",
                    foreground = "Black",
                    background = "White",
                    anchor = CENTER,
                    font = 'Comic-sans 25 bold underline').pack()





my_tree = ttk.Treeview(root)

# Define our columns
my_tree['columns'] = ("ID", "Name", "Series", "Release", "Ratio", "Theme", "Price", "Purchased")

# Format our columns
my_tree.column("#0", width=0, stretch=NO) # Ghost column
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Name", anchor=W, width=160)
my_tree.column("Series", anchor=W, width=160)
my_tree.column("Release", anchor=CENTER, width=120)
my_tree.column("Ratio", anchor=CENTER, width=80)
my_tree.column("Theme", anchor=CENTER, width=120)
my_tree.column("Price", anchor=CENTER, width=80)
my_tree.column("Purchased", anchor=CENTER, width=120)

# Create Headings
my_tree.heading("#0", text="", anchor=W) # Ghost column
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Series", text="Series", anchor=W)
my_tree.heading("Release", text="Release", anchor=CENTER)
my_tree.heading("Ratio", text="Ratio", anchor=CENTER)
my_tree.heading("Theme", text="Theme", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)
my_tree.heading("Purchased", text="Purchased from:", anchor=CENTER)



# Add Data
# my_tree.insert(parent='', index='end', iid=0, text="Parent", values=("Anakin Skywalker", "1", "Star Wars TVC"))

# Loop to add data from list
'''
data = [
       ['Darth Vader', 2, 'Star Wars'],
       ['C-3PO', 3, 'Star Wars']
]
'''
count=0
for record in Data:
    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
    count +=1

# Add child
# my_tree.insert(parent='',index='end', iid=2, text="Child", values=("Luke Skywalker", "1.2", "Star Wars TVC"))
# my_tree.move('2', '0', '0')

my_tree.pack(pady=20)


# Total of Star Wars Figures
listSW = 0
for i in Data:
    if "Star Wars" in i[5]:
        listSW +=1

swLabel = Label(root,
                    text = f'Star Wars Figures: {listSW}',
                    font = 'Helvetica 20 bold underline').pack()


# Total of Black Series
list_1 = 0
for i in Data:
    print(i)
    if "Star Wars The Black Series" in i[2]:
        list_1 += 1

TBSlabel = Label(root,
                        text = f'The Black Series : {list_1}',
                        font = 'Helvetica 15').pack()

# Total of Vintage Collection
list_2 = 0
for i in Data:
    if "The Vintage Collection" in i[2]:
        list_2 +=1

TVClabel = Label(root,
                        text= f'The Vintage Collection: {list_2}',
                        font = 'Helvetica 15').pack()

# Total of Marvel Figures
listM = 0
for i in Data:
    if "Marvel" in i[5]:
        listM += 1

mLabel = Label(root,
                    text = f'Marvel Figures: {listM}',
                    font = 'Helvetica 20 bold underline').pack()

# Total of Marvel Universe
list_mu = 0
for i in Data:
    if "Marvel Universe" in i[2]:
        list_mu +=1

MUlabel = Label(root,
                    text = f'Marvel Universe 3.75 Figures: {list_mu}',
                    font = 'Helvetica 15').pack()

# Total of Marvel Legends
list_ml = 0
for i in Data:
    if "Marvel Legends" in i[2]:
        list_ml += 1

MLlabel = Label(root,
                    text = f'Marvel Legends Figures: {list_ml}',
                    font = 'Helvetica 15').pack()

# Total of Transformers
listT = 0
for i in Data:
    if "Transformers" in i[5]:
        listT += 1

TLabel = Label(root,
                    text = f'Transformers Figures: {listT}',
                    font = 'Helvetica 20 bold underline ').pack()


# Total of Power Rangers
listPR = 0
for i in Data:
    if "Power Rangers" in i[5]:
        listPR += 1

prLabel = Label(root,
                    text = f'Power Rangers Figures: {listPR}',
                    font = 'Helvetica 20 bold underline').pack()

# Total of DC figures
listDC = 0
for i in Data:
    if "DC" in i[5]:
        listDC += 1

dcLabel = Label(root,
                    text = f'DC Figures: {listDC}',
                    font = 'Helvetica 20 bold underline').pack()

# Total number of Clone/Storm troopers
listSC = 0
listSCNames = []
for i in Data:
    if 'Storm' in i[1]:
        listSC +=1
        listSCNames.append(i[1])

print()
print(listSCNames)

scLabel = Label(root,
                    text = f'Stormtroopers: {listSC}',
                    font = 'Helvetica 20 bold underline').pack()

# Total from Amazon
list_amazon = 0
for i in Data:
    if "Amazon" in i[7]:
        list_amazon += 1

amLabel = Label(root,
                    text =f'Purchased from Amazon: {list_amazon}',
                    font = 'Helvetica 15 bold').pack()

# Total from Target
list_target = 0
for i in Data:
    if "Target" in i[7]:
        list_target += 1

targetLabel = Label(root,
                        text = f'Purcased from Target: {list_target}',
                        font = 'Helvetica 15 bold').pack()



# Total figures
totalFigures = len(Data)
Totallabel = Label(root,
                            text=f'Total Number of Figures: {totalFigures}',
                            font = 'Helvetica 20 bold underline').pack()

# Total 3.75
list_375 = 0
for i in Data:
        if '3.75"' in i[4]:
            list_375 += 1

label_375 = Label(root,
                        text = f'3.75" Figures: {list_375}',
                        font = 'Helvetica 15').pack()

# Total 6
list_6 = 0
for i in Data:
    if '6' in i[4]:
        list_6 += 1

list_6 = Label(root,
                    text = f'6" Figures: {list_6}',
                    font = 'Helvetia 15').pack()

# Total value
list_3 = []
for i in Data:
    if i[6]:
        x = float(i[6])
        list_3.append(x)

totalList_3 = sum(list_3)
TotalValue = Label(root,
                            text=f'Estimated Value of Collection: $ {round(totalList_3)}',
                            font = 'Helvetica 15 bold').pack()

#adding a 2nd column

# my_tree2 = ttk.Treeview(root)
# my_tree2['columns'] = ('Test','Test 2')

# my_tree2.column("#0", width=0, stretch=NO) #ghost column
# my_tree2.column("Test", anchor=CENTER, width=80)
# my_tree2.column("Test 2", anchor=CENTER, width=80)

# my_tree2.heading("#0", text="", anchor=W) #ghost column
# my_tree2.heading("Test", text="Test", anchor=CENTER)
# my_tree2.heading("Test 2", text="Test 2", anchor=CENTER)

# my_tree2.pack(pady=20)


# Creating a themed button
button = ttk.Button(root, text="Quit", command=root.destroy)
button.pack(pady=20)

root.mainloop()
