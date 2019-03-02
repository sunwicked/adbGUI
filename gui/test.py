import Tkinter
import os

from tkinter import filedialog

top = Tkinter.Tk()





def disconnect_call_back():
    os.system("adb disconnect")


def uninstall_call_back():
    os.system("adb uninstall" + "")  # get package name


def reboot_call_back():
    os.system("adb reboot")

def pick_apk_callback():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    os.system("adb install " + filename)


Pick = Tkinter.Button(top, bg="#000000", text="Pick file", command=pick_apk_callback)
Disconnect = Tkinter.Button(top, bg="#000000", text="ADB disconnect", command=disconnect_call_back)
Uninstall = Tkinter.Button(top, bg="#000000", text="ADB uninstall", command=uninstall_call_back)
Reboot = Tkinter.Button(top, bg="#000000", text="ADB reboot", command=reboot_call_back)

Pick.pack()
Disconnect.pack()
Uninstall.pack()
Reboot.pack()
top.mainloop()
