from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from vpnservice import start_vpn, stop_vpn

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.btn = Button(text="ВКЛ VPN", font_size=24)
        self.btn.bind(on_press=self.toggle)
        self.add_widget(self.btn)

        self.enabled = False

    def toggle(self, *args):
        if not self.enabled:
            start_vpn()
            self.btn.text = "ВЫКЛ VPN"
        else:
            stop_vpn()
            self.btn.text = "ВКЛ VPN"

        self.enabled = not self.enabled

class WGApp(App):
    def build(self):
        return MainUI()

if __name__ == "__main__":
    WGApp().run()
