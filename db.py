from Tkinter import *
import MySQLdb
import tkMessageBox
import csv
import os
#from tempfile import NamedTemporaryFile
#import shutil
#from PIL import ImageTk, Image
tkmain = Tk()
tkmain.title("Registration")
db = MySQLdb.connect(host="mannu", user="personal", passwd="", db="test")
cur = db.cursor()
if not (os.path.isfile("combined_file.csv")):
	with open('combined_file.csv', 'w+') as outcsv:
		writer = csv.DictWriter(outcsv,["ID", "Name", "DOB","Gender","Blood_group","Address","State","City","Mobile","E-mail","Flage"])
		writer.writeheader()

def insertfun():
	Id=str(entryId.get())
	name=str(entryName.get())
	dob=str(entryDob.get())
	sex=str(v.get())	
	bg=str(variableBG.get())
	add=str(entryAddress.get("1.0",END))
	state=str(variableState.get())
	city=str(variableCity.get())
	mob=str(entryMobile.get())
	mail=str(entryEmail.get())
	cur.execute("INSERT INTO personal VALUES('"+Id+"','"+name+"','"+dob+"','"+sex+"','"+bg+"','"+add+"','"+state+"','"+city+"','"+mob+"','"+mail+"')")
	db.commit()
	with open('combined_file.csv', 'a') as outcsv:
		writer = csv.writer(outcsv)
		writer.writerow([Id,name,dob,sex,bg,add,state,city,mob,mail,"1"])


def updatefun():
	Id=str(entryId.get())
	name=str(entryName.get())
	dob=str(entryDob.get())
	sex=str(v.get())	
	bg=str(variableBG.get())
	add=str(entryAddress.get("1.0",END))
	state=str(variableState.get())
	city=str(variableCity.get())
	mob=str(entryMobile.get())
	mail=str(entryEmail.get())
	cur.execute("UPDATE personal set name='"+name+"',DOB='"+dob+"',Gender='"+sex+"',Blood_group='"+bg+"',Address='"+add+"',State='"+state+"',city='"+city+"',mobile='"+mob+"',mail='"+mail+"' WHERE id='"+Id+"'")
	db.commit()
	with open('combined_file.csv', 'a') as outcsv:
		writer = csv.writer(outcsv)
		writer.writerow([Id,name,dob,sex,bg,add,state,city,mob,mail,"0"])
	
	with open('combined_file.csv', 'rb') as inp, open('tmp_old_report.csv', 'w') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):
			if row[9]!=0:
				writer.writerow(row)
			else:
				writer.writerow(row)
	# os.remove("combined_file.csv")

def viewfun():
	strg=""
	Id=str(entryId.get())
	cur.execute("select * from personal where id='"+Id+"'")
	for row in cur.fetchall():
		strg+="Id="+Id+"\nName="+row[1]+"\nDOB="+str(row[2])+"\nGender="+row[3]+"\nBlood-Group="+row[4]+"\nAddress="+row[5]+"\nState="+row[6]+"\nCity="+row[7]+"\nMobile="+str(row[8])+"\nemail-id="+row[9]
	tkMessageBox.showinfo("Information",strg)

def deletefun():
	Id=str(entryId.get())
	cur.execute("delete from personal where id='"+Id+"'")
	db.commit()

root = Frame(tkmain, bg='cyan', width = 500, height=250, pady=3,padx=3).grid(row=0, columnspan=4,rowspan=5)

labelId = Label(root,text="ID").grid(row=0,column=0,sticky=W)
entryId = Entry(root)
entryId.grid(row=0,column=1,sticky=W)

labelName = Label(root,text="Name").grid(row=1,column=0,sticky=W)
entryName = Entry(root)
entryName.grid(row=1,column=1,sticky=W)

labelDob = Label(root,text="DOB").grid(row=2,column=0,sticky=W)
entryDob = Entry(root)
entryDob.grid(row=2,column=1,sticky=W)

labelGender = Label(root,text="Gender").grid(row=3,column=0,sticky=W)
v = StringVar()
maleRadio=Radiobutton(root, text="Male", variable=v, value="Male")
maleRadio.grid(row=3,column=1,sticky=W)
femaleRadio=Radiobutton(root, text="Female", variable=v, value="Female")
femaleRadio.grid(row=3,column=2,sticky=W)

labelBloodGroup = Label(root,text="Blood Group")
labelBloodGroup.grid(row=4,column=0,sticky=W)
variableBG = StringVar(root)
variableBG.set("O+") # default value
entryBloodGroup = OptionMenu(root, variableBG, "O+", "A+", "B+","AB+","O-", "A-", "B-","AB-")
entryBloodGroup.grid(row=4,column=1,sticky=W)

#img = ImageTk.PhotoImage(Image.open("BackUp/DR-avatar.png"))
#label = Label(root,image=img,height=100,width=100)
#label.grid(row=4,column=2,sticky=W)
#label.image = img # keep a reference!

tk = Frame(tkmain, bg='Blue', width = 500, height=250, pady=3,padx=3).grid(row=5, columnspan=4,rowspan=5)
labelAddress = Label(tk,text="Address")
labelAddress.grid(row=5,column=0,sticky=W)
entryAddress = Text(tk,height=2,width=15)
entryAddress.grid(row=5,column=1,sticky=W)

labelState = Label(tk,text="State")
labelState.grid(row=6,column=0,sticky=W)
variableState = StringVar(tk)
variableState.set("Maharashtra") # default value
entryState = OptionMenu(tk, variableState, "AP", "West Bengal", "Uttarakhand", "Punjab", "Rajasthan", "Odisha","Meghalaya","Mizoram","Jharkhand","Kerala","Karnataka","Maharashtra")
entryState.grid(row=6,column=1,sticky=W)



labelCity = Label(tk,text="City")
labelCity.grid(row=6,column=2,sticky=W)
variableCity = StringVar(tk)
variableCity.set("Pune") # default value
entryCity = OptionMenu(tk, variableCity, "Pune","Mumbai", "Kolkata", "Assam","Hydrabad","Bangluru", "udaipur", "manipur","Aurangabad","Jamshedpur","Ranchi","vizag","Bhubneswar")
entryCity.grid(row=6,column=3,sticky=W)

labelMobile = Label(tk,text="Mobile Number")
labelMobile.grid(row=7,column=0,sticky=W)
entryMobile = Entry(tk)
entryMobile.grid(row=7,column=1,sticky=W)

labelEmail = Label(tk,text="Email")
labelEmail.grid(row=8,column=0,sticky=W)
entryEmail = Entry(tk)
entryEmail.grid(row=8,column=1,sticky=W,pady=5)


insert = Button(tk, text="Insert",command=insertfun).grid(row=9,column=0,sticky=W)
update = Button(tk, text="Update",command=updatefun).grid(row=9,column=1,sticky=W)
delete = Button(tk, text="Delete",command=deletefun).grid(row=9,column=2,sticky=W)
view   = Button(tk, text="View",command=viewfun).grid(row=9,column=3,sticky=E)

tkmain.mainloop()
