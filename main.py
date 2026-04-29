from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
        try:
            with open("/sdcard/test_log.txt", "w") as f:
                f.write("APP STARTED SUCCESSFULLY")
        except Exception as e:
            pass
        return Label(text="Hello APK")

MyApp().run()
