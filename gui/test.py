import subprocess
import os
import tkinter
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))
LOGCAT_FILE_PATH = dir_path + "/log.txt"
ip = "0.0.0.0:5555"
package = "test"
log = ""

top = tkinter.Tk()


def disconnect_call_back():
    console_log = subprocess.run(['adb', 'disconnect'], stdout=subprocess.PIPE)
    convert_to_str(console_log)


def connect_call_back():
    global ip
    ip = entry.get()
    ip_value['text'] = ip
    console_log = subprocess.run(['adb', 'connect', 'ip'], stdout=subprocess.PIPE)
    convert_to_str(console_log)


def reboot_call_back():
    console_log = subprocess.run(['adb', 'reboot'], stdout=subprocess.PIPE)
    convert_to_str(console_log)


def pick_apk_callback():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    global package
    package = subprocess.run(
        ['aapt', 'dump', 'badging', filename],
        stdout=subprocess.PIPE
    )
    std_out = str(package.stdout)
    if std_out:
        package = std_out.split("versionCode")[0]
        package = package.split("'")[1]
        package_value['text'] = package
        subprocess.run(
            ['adb', 'install', filename],
            stdout=subprocess.PIPE)
    else:
        print("failed")


def uninstall_call_back():
    console_log = subprocess.run(['adb', 'uninstall', package], stdout=subprocess.PIPE)
    convert_to_str(console_log)


def logcat_to_file_callback():
    os.system("adb logcat > " + LOGCAT_FILE_PATH)  # get package name


def clear_call_back():
    console_log = subprocess.run(['adb', 'shell', 'pm', 'clear', package], stdout=subprocess.PIPE)
    convert_to_str(console_log)


def convert_to_str(input_val):
    log_value['text'] = str(input_val.stdout)


label = tkinter.Label(top, text=" Enter IP ")
label.grid(row=0, column=0)

entry = tkinter.Entry(top)
entry.grid(row=0, column=1)

connect = tkinter.Button(top, text="ADB connect", command=connect_call_back)
connect.grid(row=0, column=2)
pick = tkinter.Button(top, bg="#000000", text=" ADB install ", command=pick_apk_callback)
pick.grid(row=2, column=0)

disconnect = tkinter.Button(top, bg="#000000", text=" ADB disconnect ", command=disconnect_call_back)
disconnect.grid(row=3, column=0)
uninstall = tkinter.Button(top, bg="#000000", text=" ADB uninstall ", command=uninstall_call_back)
uninstall.grid(row=4, column=0)
reboot = tkinter.Button(top, bg="#000000", text=" ADB reboot ", command=reboot_call_back)
reboot.grid(row=5, column=0)
clear = tkinter.Button(top, bg="#000000", text=" ADB clear ", command=clear_call_back)
clear.grid(row=6, column=0)
# Logcat = tkinter.Button(top, bg="#000000", text="ADB logcat", command=logcat_to_file_callback)
# Logcat.grid(row=7, column=0)
ip_label = tkinter.Label(top, text=" IP::")
ip_label.grid(row=8, column=0)
ip_value = tkinter.Label(top, text=ip)
ip_value.grid(row=8, column=1)
package_label = tkinter.Label(top, text=" Package Name::")
package_label.grid(row=9, column=0)
package_value = tkinter.Label(top, text=package)
package_value.grid(row=9, column=1)
log_label = tkinter.Label(top, text=" Log::")
log_label.grid(row=10, column=0)
log_value = tkinter.Label(top, text=log)
log_value.grid(row=10, column=1)

top.mainloop()
