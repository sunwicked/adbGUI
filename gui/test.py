import Tkinter
import tkMessageBox
import os

top = Tkinter.Tk()


def disconnect_call_back():
    tkMessageBox.showinfo("Hello Python", "Hello World")
    os.system("adb disconnect")


def uninstall_call_back():
    tkMessageBox.showinfo("Hello Python", "Hello World")
    os.system("adb install" + "")


Disconnect = Tkinter.Button(top, bg="#000000", text="ADB disconnect", command=disconnect_call_back)
Uninstall = Tkinter.Button(top, bg="#000000", text="ADB install", command=uninstall_call_back)

Disconnect.pack()
Uninstall.pack()
top.mainloop()
