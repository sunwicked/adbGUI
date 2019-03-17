import Tkinter
import os
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))
PACKAGE_FILE_PATH = dir_path + "/name.txt"

top = Tkinter.Tk()

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
    global package
    package = f.read().split("'")[1]
    os.system("adb install " + filename)


def uninstall_call_back():
    print package
    os.system("adb uninstall" + package)  # get package name


Label = Tkinter.Label(top, text="Enter IP")
Label.grid(row=0, column=0)

Entry = Tkinter.Entry(top)
Entry.grid(row=0, column=1)

Connect = Tkinter.Button(top, text="ADB connect", command=connect_call_back)
Connect.grid(row=1, column=1)
Pick = Tkinter.Button(top, bg="#000000", text="Pick file", command=pick_apk_callback)
Disconnect = Tkinter.Button(top, bg="#000000", text="ADB disconnect", command=disconnect_call_back)
Uninstall = Tkinter.Button(top, bg="#000000", text="ADB uninstall", command=uninstall_call_back)
Reboot = Tkinter.Button(top, bg="#000000", text="ADB reboot", command=reboot_call_back)

Label.pack()
Entry.pack()
Connect.pack()
Pick.pack()
Disconnect.pack()
Uninstall.pack()
Reboot.pack()
top.mainloop()
