from tkinter import *
from turtle import update

root = Tk()
root.geometry("400x400")
root.title("ADV-177 Project")

label_name = Label(root, text="Name: ")
label_name.place(relx=0.3,rely=0.1, anchor= CENTER)
input_name = Entry(root)
input_name.place(relx=0.6,rely=0.1, anchor= CENTER)
label_password = Label(root, text="Password: ")
label_password.place(relx=0.3,rely=0.2, anchor= CENTER)
input_password = Entry(root)
input_password.place(relx=0.6,rely=0.2, anchor= CENTER)
label_captcha = Label(root, text="Captcha: ")
label_captcha.place(relx=0.3,rely=0.3, anchor= CENTER)
input_captcha = Entry(root)
input_captcha.place(relx=0.6,rely=0.3, anchor= CENTER)
label_show_name = Label(root)
label_show_name.place(relx=0.5,rely=0.7, anchor= CENTER)
label_show_password = Label(root)
label_show_password.place(relx=0.5,rely=0.8, anchor= CENTER)
label_show_captcha = Label(root)
label_show_captcha.place(relx=0.5,rely=0.9, anchor= CENTER)

class userDB():

  def __init__(self):
    self.__name = "John"
    self.__password = "JohnSaidHello"
    self.captcha = "Johnny"

  def showuser(self):
    label_show_name["text"] = "Name: " + self.__name
    label_show_password["text"] = "Password: " + self.__password
    label_show_captcha["text"] = "Captcha: " + self.captcha

user = userDB()
def addUser():
  global user
  user.name = input_name.get()
  user.password = input_password.get()
  user.captcha = input_captcha.get()

updateData = Button(root,text="Update Data", command=addUser)
updateData.place(relx=0.3,rely=0.5,anchor=CENTER)
showProfile = Button(root,text="Show Profile", command=user.showuser)
showProfile.place(relx=0.7,rely=0.5,anchor=CENTER)

root.mainloop()