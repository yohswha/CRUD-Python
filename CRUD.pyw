
#***********************************************************
# YOHSWHA ENMANUEL BELLO CUEVAS, MATRICULA: 100376295      *
#***********************************************************


from tkinter import *
from tkinter import messagebox
import sqlite3


#*****************************************
#                FUNCTIONS               #  
# ****************************************
def connectionDDBB():
    
    myConnection = sqlite3.connect("Usuarios.db")
    myCursor=myConnection.cursor()
    
    try:
        myCursor.execute('''
                CREATE TABLE DATAUSERS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME VARCHAR(50),
                LASTNAME VARCHAR(50),
                PASSWORD VARCHAR(50),
                ADDRESS VARCHAR(100),
                COMMENTS VARCHAR(300))
                ''')
        messagebox.showinfo("BBDD", "Base de Datos creado Exitosamente")
    except:
        messagebox.showwarning("!Atencion", "Base de Datos Existente")      


def closeApp():
    valor=messagebox.askquestion("salir", "¿Deseas Salir?")
    if valor=="yes":
        root.destroy()
        
        
def clearFields():
    myId.set("")
    myName.set("")
    myLastName.set("")
    myPass.set("")
    myAddress.set("")
    commentArea.delete(1.0,END)
 
    
def createUser():
    myConnection = sqlite3.connect("Usuarios.db")
    myCursor=myConnection.cursor()
    myCursor.execute("INSERT INTO DATAUSERS VALUES(NULL,'"+myName.get()+"','"
                     +myLastName.get()+"','"+myPass.get()+"','"+myAddress.get()+"','"
                     +commentArea.get(1.0,END) +"')")
    
    myConnection.commit()
    messagebox.showinfo("Felicidades","Usuario Guardado Exitosamente")
    clearFields()
    
def showUser():
    myConnection = sqlite3.connect("Usuarios.db")
    myCursor=myConnection.cursor()
    myCursor.execute("SELECT * FROM DATAUSERS WHERE ID="+myId.get())
    user=myCursor.fetchall()
    try:    
        for usuario in user:
            myId.set(usuario[0])
            myName.set(usuario[1])
            myLastName.set(usuario[2])
            myPass.set(usuario[3])
            myAddress.set(usuario[0])
            commentArea.insert(1.0,usuario[5])
        
        myConnection.commit()
    except:
        messagebox.showwarning("Atencion","no hay registros con este ID")
        
def updateUser():
    myConnection = sqlite3.connect("Usuarios.db")
    myCursor=myConnection.cursor()
    try:

        myCursor.execute("UPDATE DATAUSERS SET USERNAME='"+myName.get()+
                         "',LASTNAME='"+myLastName.get()+
                         "',ADDRESS='"+myAddress.get()+"',COMMENTS='"+commentArea.get(1.0,END)+
                         "' WHERE ID="+myId.get()) 
        
        myConnection.commit()
        messagebox.showinfo("Felicidades","datos Actualizados Correctamente")
    except:
        messagebox.showwarning("Atencion","no hay registros con este ID")

        
def deleteUser():
    myConnection = sqlite3.connect("Usuarios.db")
    myCursor=myConnection.cursor()
    try:
        myCursor.execute("DELETE FROM DATAUSERS WHERE ID="+myId.get())
        if myCursor.rowcount()>0:
            myConnection.commit()
            messagebox.showwarning("Atencion","Usuario Eliminado Correctamente")
            clearFields()

    except:
         messagebox.showwarning("Atencion","no hay registros con este ID")

    
root=Tk()


#***********************************************
#                   BARRA DE MENU              #
# **********************************************
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height= 300)
#-----------------BBDD Option-----------------#
bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar", command=connectionDDBB)
bbddMenu.add_command(label="Salir", command=closeApp)
#-----------------Borrar Option-----------------#

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar Campos",command=clearFields)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=createUser)
crudMenu.add_command(label="Leer", command=showUser)
crudMenu.add_command(label="Actualizar",command=updateUser)
crudMenu.add_command(label="Borrar",command=deleteUser)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de....")


barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)


#********************************************
#                    FORMULARIO             #            
# *******************************************

myFrame=Frame(root)
myFrame.pack()

myId=StringVar()
myName=StringVar()
myLastName=StringVar()
myPass=StringVar()
myAddress=StringVar()
comment=StringVar()


idField=Entry(myFrame,textvariable=myId)
idField.grid(row=0,column=1,padx=10, pady=10)

nameField=Entry(myFrame,textvariable=myName)
nameField.grid(row=1,column=1,padx=10, pady=10)

lastName=Entry(myFrame,textvariable=myLastName)
lastName.grid(row=2,column=1,padx=10, pady=10)

passWord=Entry(myFrame,textvariable=myPass)
passWord.grid(row=3,column=1,padx=10, pady=10)
passWord.config(show="*")

addressField=Entry(myFrame,textvariable=myAddress)
addressField.grid(row=4,column=1,padx=10, pady=10)


commentArea=Text(myFrame, width=16, height= 5)
commentArea.grid(row=5,column=1,padx=10, pady=10)
scrollVert=Scrollbar(myFrame, command=commentArea.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")

commentArea.config(yscrollcommand=scrollVert.set)

#*******************Lables de los campos***********************

idLabel=Label(myFrame, text="ID:")
idLabel.grid(row=0,column=0,sticky="e", padx=10,pady=10)

nameLabel=Label(myFrame, text="Nombre:")
nameLabel.grid(row=1,column=0,sticky="e", padx=10,pady=10)

lastNameLabel=Label(myFrame, text="Apellidos:")
lastNameLabel.grid(row=2,column=0,sticky="e", padx=10,pady=10)

passLabel=Label(myFrame, text="Password:")
passLabel.grid(row=3,column=0,sticky="e", padx=10,pady=10)

addressLabel=Label(myFrame, text="Dirrecion:")
addressLabel.grid(row=4,column=0,sticky="e", padx=10,pady=10)

commentLabel=Label(myFrame, text="Comentario:")
commentLabel.grid(row=5,column=0,sticky="e", padx=10,pady=10)

##*********************Botones***********************

myFrame2=Frame()
myFrame2.pack()

createButton=Button(myFrame2, text="Crear",command=createUser)
createButton.grid(row=1,column=0,sticky="e", padx=10, pady=10)

readButton=Button(myFrame2, text="Leer",command=showUser)
readButton.grid(row=1,column=1,sticky="e", padx=10, pady=10)

updateButton=Button(myFrame2, text="Actualizar",command=updateUser)
updateButton.grid(row=1,column=2,sticky="e", padx=10, pady=10)

deleteButton=Button(myFrame2, text="Borrar",command=deleteUser)
deleteButton.grid(row=1,column=3,sticky="e", padx=10, pady=10)


root.mainloop()
