import os

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

package = "com.test"
dir_path = os.path.dirname(os.path.realpath(__file__))
PACKAGE_FILE_PATH = dir_path + "/name.txt"


def disconnect_call_back(args):
    os.system("adb disconnect")


def reboot_call_back(args):
    os.system("adb reboot")


def connect_call_back(args):
    os.system("adb connect " + ip)


def uninstall_call_back(args):
    # print(package)
    os.system("adb uninstall" + package)  # get package name


def pick_apk_intall_callback(args):
    filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    os.system("aapt dump badging " + filename + " | awk 'NR==1{print $2}' > " + PACKAGE_FILE_PATH)
    f = open(PACKAGE_FILE_PATH, 'r')
    global package
    package = f.read().split("'")[1]
    os.system("adb install " + filename)


class KivyButton(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.box_ip = BoxLayout(orientation='horizontal', spacing=20)
        self.btn_install = Button(
            text="ADB connect",
            size_hint=(.3, .1),
            on_press=connect_call_back
        )
        self.btn_uninstall = Button(
            text="ADB uninstall",
            size_hint=(.3, .1),
            on_press=uninstall_call_back
        )
        self.btn_reboot = Button(
            text="ADB reboot",
            size_hint=(.3, .1),
            on_press=reboot_call_back
        )
        self.btn_disconnect = Button(
            text="ADB disconnect",
            size_hint=(.3, .1),
            on_press=disconnect_call_back
        )
        self.txt = TextInput(hint_text='Input IP', size_hint=(.5, .1))

    def build(self):
        self.box_ip.add_widget(self.txt)
        self.box_ip.add_widget(self.btn_install)
        self.box.add_widget(self.box_ip)
        self.box.add_widget(self.btn_disconnect)
        self.box.add_widget(self.btn_uninstall)
        self.box.add_widget(self.btn_reboot)
        return self.box


KivyButton().run()
