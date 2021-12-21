from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

taz = Tk()
width = taz.winfo_screenwidth()
print(width)
height = taz.winfo_screenheight()

##################### database connection ######################

tazTV = ttk.Treeview(height=10, columns=('Item Name', 'Rate', 'Type'))


################## for char input  ###############

def only_char_input(P):
    if P.isalpha() or P == '':
        return True
    return False


callback = taz.register(only_char_input)


# for digit
def only_numeric_input(P):
    if P.isdigit() or P == '':
        return True
    return False


callback2 = taz.register(only_numeric_input)


def dbconfig():
    global conn, mycursor
    conn = pymysql.connect(host="localhost", user="root", db="training")
    mycursor = conn.cursor()


################### Clear Screen#####################

def clear_Screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()


def mainheading():
    label = Label(taz, text="Hotel Management System", fg="red", bg="yellow", font=("Comic Sans Ms", 40, "bold"),
                  padx=350, pady=0)
    label.grid(row=0, columnspan=4)


usernameVar = StringVar()
passwordVar = StringVar()


def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    labellogin = Label(taz, text="Admin Login", font=("ariel", 25, "bold"))
    labellogin.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    usernameLabel = Label(taz, text="User Name", font=("ariel", 20, "bold"))
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="User Password", font=("ariel", 20, "bold"))
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="Green", bd=10, command=adminLogin)
    loginButton.grid(row=4, column=1, columnspan=2, padx=20, pady=5)


###################### Logout ###########
def logout():
    clear_Screen()
    mainheading()
    loginwindow()


def welcomewindow():
    clear_Screen()
    mainheading()
    welcome = Label(taz, text="Welcome Admin", font=("ariel", 25, "bold"))
    welcome.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="Green", bd=10, command=logout)
    logoutButton.grid(row=4, column=1, columnspan=2, padx=20, pady=5)

    manageRest = Button(taz, text="Manage Hotel", width=20, height=2, fg="green", bd=2, command=additemWindow)
    manageRest.grid(row=5, column=1, columnspan=2, padx=20, pady=10)

    billGen = Button(taz, text="Bill Generation", width=20, height=2, fg="red", bd=2, command=billwindow)
    billGen.grid(row=6, column=1, columnspan=2, padx=20, pady=10)


####################### back Button ##############

def back():
    clear_Screen()
    mainheading()
    welcomewindow()


itemnameVar = StringVar()
itemrateVar = StringVar()
itemtypeVar = StringVar()


##################################################
def getItemInTreeview():
    # to delete already inserted data----
    records = tazTV.get_children()
    for x in records:
        tazTV.delete(x)
    conn = pymysql.connect(host="localhost", user="root", db="training")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    # print(mycursor)
    query1 = "select * from itemlist"
    mycursor.execute(query1)
    data = mycursor.fetchall()
    # print(data)
    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"], row['item_type']))
    conn.close()
    tazTV.bind("<Double-1>", OnDoubleClick)


######################## Double Click  ####################

def OnDoubleClick(event):
    item = tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemtypeVar.set(item_detail[1])


############################# update item ######################

def updateItem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemtypeVar.get()
    dbconfig()
    que = "update itemlist set item_rate=%s,item_type=%s where item_name=%s"
    val = (rate, type, name)
    mycursor.execute(que, val)
    conn.commit()
    messagebox.showinfo("Updation Confirmation", "Item updated Successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()


############################# Delete item ######################

def deleteItem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemtypeVar.get()
    dbconfig()
    que1 = "delete from itemlist where item_name=%s"
    val = (name)
    mycursor.execute(que1, val)
    conn.commit()
    messagebox.showinfo("Delete Confirmation", "Item Delete Successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()


def additemWindow():
    clear_Screen()
    mainheading()
    additem = Label(taz, text="Insert item", font=("ariel", 25, "bold"))
    additem.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    itemnameLabel = Label(taz, text="Item Name", font=("ariel", 20, "bold"))
    itemnameLabel.grid(row=2, column=1, padx=20, pady=5)

    itemrateLabel = Label(taz, text="Item Rate(INR)", font=("ariel", 20, "bold"))
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemtypeLabel = Label(taz, text="Item Type", font=("ariel", 20, "bold"))
    itemtypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)

    # for validation
    itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    itemtypeEntry = Entry(taz, textvariable=itemtypeVar)
    itemtypeEntry.grid(row=4, column=2, padx=20, pady=5)
    itemtypeEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="Green", bd=10, command=additemprocess)
    additemButton.grid(row=3, column=3, columnspan=1)

    updateButton = Button(taz, text="Update Item", width=20, height=2, fg="Green", bd=10, command=updateItem)
    updateButton.grid(row=4, column=3, columnspan=1)

    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="Green", bd=10, command=deleteItem)
    deleteButton.grid(row=5, column=3, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="Green", bd=10, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)

    backButton = Button(taz, text="Back", width=20, height=2, fg="Green", bd=10, command=back)
    backButton.grid(row=4, column=0, columnspan=1)

    ################# TreeVeiw  #################

    tazTV.grid(row=8, columnspan=3)
    # style=ttk.Style(taz)
    # style.theme_use('calm')
    # style.configure("TreeView",fieldbackground="green")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=8, column=2, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)
    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")

    getItemInTreeview()


def additemprocess():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemtypeVar.get()

    dbconfig()
    query = "insert into itemlist(item_name,item_rate,item_type)values(%s,%s,%s)"
    val = (name, rate, type)
    mycursor.execute(query, val)
    conn.commit()
    messagebox.showinfo("Save Item", "Item Saved successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()


################## bill Window ###############
global x
x = datetime.now()
datetimeVar = StringVar()
datetimeVar.set(x)
customerNameVar = StringVar
mobileVar = StringVar
combovaraiable = StringVar
baserate = StringVar


#################### Combo data ###############
def combo_input():
    dbconfig()
    mycursor.execute('select item_name from itemlist')
    data = []
    for row in mycursor.fetchall():
        data.append(row[0])
    return data


################### optioncallback ###############

def optionCallBack(*args):
    global itemname
    itemname = combovaraiable.get()
    print(itemname)


def billwindow():
    clear_Screen()
    mainheading()
    billitem = Label(taz, text="Generate Bill", font=("ariel", 25, "bold"))
    billitem.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="Green", bd=10, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)

    backButton = Button(taz, text="Back", width=20, height=2, fg="Green", bd=10, command=back)
    backButton.grid(row=4, column=0, columnspan=1)

    dateTimeLabel = Label(taz, text="Date & Time", font=("ariel", 15, "bold"))
    dateTimeLabel.grid(row=2, column=1, padx=20, pady=5)

    dateTimeEntry = Entry(taz, textvariable=datetimeVar, font=("ariel", 15, "bold"))
    dateTimeEntry.grid(row=2, column=2, padx=20, pady=5)

    customerNameLabel = Label(taz, text="Customer Name", font=("ariel", 15, "bold"))
    customerNameLabel.grid(row=3, column=1, padx=20, pady=5)

    customerNameEntry = Entry(taz, textvariable=customerNameVar, font=("ariel", 15, "bold"))
    customerNameEntry.grid(row=3, column=2, padx=20, pady=5)
    customerNameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    mobileLabel = Label(taz, text="Contact No", font=("ariel", 15, "bold"))
    mobileLabel.grid(row=4, column=1, padx=20, pady=5)

    mobileEntry = Entry(taz, textvariable=mobileVar, font=("ariel", 15, "bold"))
    mobileEntry.grid(row=4, column=2, padx=20, pady=5)
    mobileEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    selectLabel = Label(taz, text="Select Item", font=("ariel", 15, "bold"))
    selectLabel.grid(row=5, column=1, padx=20, pady=5)

    l = combo_input()
    c = ttk.Combobox(taz, values=l, textvariable=combovaraiable, font=("ariel", 15, "bold"))
    c.set("select Item")
    combovaraiable.trace('w', optionCallBack)
    c.grid(row=5, column=2, padx=20, pady=5)

    rateLabel = Label(taz, text="Item Rate", font=("ariel", 15, "bold"))
    rateLabel.grid(row=6, column=1, padx=20, pady=5)

    rateEntry = Entry(taz, textvariable=baserate, font=("ariel", 15, "bold"))
    rateEntry.grid(row=6, column=2, padx=20, pady=5)


def adminLogin():
    dbconfig()
    username = usernameVar.get()
    password = passwordVar.get()
    que = "select * from user_info where user_id=%s and user_pass=%s"
    var = (username, password)
    mycursor.execute(que, var)
    data = mycursor.fetchall()
    flag = False
    for row in data:
        flag = True
    conn.close()

    if flag == True:
        welcomewindow()
    else:
        messagebox.showerror("Invalid User Credentail", "Either User Name or Password is Incorrect")
        usernameVar.set("")
        passwordVar.set("")


mainheading()
loginwindow()
taz.title("Hotel Taz Management System")
taz.geometry("%dx%d+0+0" % (width, height))
taz.mainloop()
