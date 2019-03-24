import os
import tkinter
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))
PACKAGE_FILE_PATH = dir_path + "/name.txt"

top = tkinter.Tk()

package = "test"


def disconnect_call_back():
    os.system("adb disconnect")


def connect_call_back():
    ip = Entry.get()
    os.system("adb connect " + ip)


def reboot_call_back():
    os.system("adb reboot")


def pick_apk_callback():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    os.system("aapt dump badging " + filename + " | awk 'NR==1{print $2}' > " + PACKAGE_FILE_PATH)
    f = open(PACKAGE_FILE_PATH, 'r')
    if not filename:
        global package
        package = f.read().split("'")[1]
        os.system("adb install " + filename)
    else:
        print("failed")


def uninstall_call_back():
    print(package)
    os.system("adb uninstall" + package)  # get package name


Label = tkinter.Label(top, text="Enter IP")
Label.grid(row=0, column=0)

Entry = tkinter.Entry(top)
Entry.grid(row=0, column=1)

Connect = tkinter.Button(top, text="ADB connect", command=connect_call_back)
Connect.grid(row=0, column=2)
Pick = tkinter.Button(top, bg="#000000", text="ADB install", command=pick_apk_callback)
Pick.grid(row=2, column=0)
Disconnect = tkinter.Button(top, bg="#000000", text="ADB disconnect", command=disconnect_call_back)
Disconnect.grid(row=3, column=0)
Uninstall = tkinter.Button(top, bg="#000000", text="ADB uninstall", command=uninstall_call_back)
Uninstall.grid(row=4, column=0)
Reboot = tkinter.Button(top, bg="#000000", text="ADB reboot", command=reboot_call_back)
Reboot.grid(row=5, column=0)

top.mainloop()
