import Tkinter
import os

from tkinter import filedialog

PACKAGE_FILE_PATH = "/Users/ken/Documents/name.txt"

top = Tkinter.Tk()


package = "test"



def disconnect_call_back():
    os.system("adb disconnect")

def reboot_call_back():
    os.system("adb reboot")

def pick_apk_callback():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    os.system("aapt dump badging " + filename + " | awk 'NR==1{print $2}' > " + PACKAGE_FILE_PATH)
    f = open(PACKAGE_FILE_PATH, 'r')
    global package
    package = f.read().split("'")[1]
    os.system("adb install " + filename)


def uninstall_call_back():
    print package
    os.system("adb uninstall" + package)  # get package name

Pick = Tkinter.Button(top, bg="#000000", text="Pick file", command=pick_apk_callback)
Disconnect = Tkinter.Button(top, bg="#000000", text="ADB disconnect", command=disconnect_call_back)
Uninstall = Tkinter.Button(top, bg="#000000", text="ADB uninstall", command=uninstall_call_back)
Reboot = Tkinter.Button(top, bg="#000000", text="ADB reboot", command=reboot_call_back)

Pick.pack()
Disconnect.pack()
Uninstall.pack()
Reboot.pack()
top.mainloop()
