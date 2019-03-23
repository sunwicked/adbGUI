import os

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView


package = "com.test"
ip = ""
dir_path = os.path.dirname(os.path.realpath(__file__))
PACKAGE_FILE_PATH = dir_path + "/name.txt"


def disconnect_call_back(args):
    os.system("adb disconnect")


def reboot_call_back(args):
    os.system("adb reboot")


def connect_call_back(args):
    os.system("adb connect " + ip)

def show_file_picker_callback(args):
    return MyWidget()


def set_ip_call_back(instance, value):
    global ip
    print(value)
    ip = value


def uninstall_call_back(args):
    print(package)
    os.system("adb uninstall" + package)  # get package name


def pick_apk_install_callback(file_path):
    os.system("aapt dump badging " + file_path + " | awk 'NR==1{print $2}' > " + PACKAGE_FILE_PATH)
    f = open(PACKAGE_FILE_PATH, 'r')
    global package
    if package.isspace():
        package = f.read().split("'")[1]
        os.system("adb install " + file_path)
    else:
        print("failed")


class MyWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        container = BoxLayout(orientation='vertical')

        filechooser = FileChooserListView()
        filechooser.bind(on_selection=lambda x: self.selected(filechooser.selection))

        open_btn = Button(text='open', size_hint=(1, .2))
        open_btn.bind(on_release=lambda x: self.open(filechooser.path, filechooser.selection))

        container.add_widget(filechooser)
        container.add_widget(open_btn)
        self.add_widget(container)

    def open(self, path, filename):
        print(filename)
        if len(filename) > 0:
            with open(os.path.join(path, filename[0])) as f:
                print(f.read())

    def selected(self, filename):
        pick_apk_install_callback(filename)


class KivyButton(App):

    def build(self):
        self.box = BoxLayout(orientation='vertical')
        self.box_ip = BoxLayout(orientation='horizontal', spacing=20)
        # Connect to Ip
        self.btn_connect = Button(
            text="ADB connect",
            size_hint=(.3, .1),
            on_press=connect_call_back
        )
        # Uninstall
        self.btn_uninstall = Button(
            text="ADB uninstall",
            size_hint=(.3, .1),
            on_press=uninstall_call_back
        )
        # Reboot device
        self.btn_reboot = Button(
            text="ADB reboot",
            size_hint=(.3, .1),
            on_press=reboot_call_back
        )
        # Disconnect all device
        self.btn_disconnect = Button(
            text="ADB disconnect",
            size_hint=(.3, .1),
            on_press=disconnect_call_back
        )
        # Install app
        self.btn_install = Button(
            text="ADB install",
            size_hint=(.3, .1),
            on_press=show_file_picker_callback
        )
        textinput = TextInput(hint_text='Input IP',
                              size_hint=(.5, .1),
                              multiline=False
                              )
        textinput.bind(text=set_ip_call_back)
        self.box_ip.add_widget(textinput)
        self.box_ip.add_widget(self.btn_connect)
        self.box.add_widget(self.box_ip)
        self.box.add_widget(self.btn_disconnect)
        self.box.add_widget(self.btn_uninstall)
        self.box.add_widget(self.btn_install)
        self.box.add_widget(self.btn_reboot)
        return self.box



KivyButton().run()
