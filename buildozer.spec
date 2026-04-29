[app]

title = My Application

package.name = myapp

package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

source.main = main.py

version = 1.0

requirements = python3==3.10.0,kivy,plyer

icon.filename = icon.png

orientation = portrait

osx.python_version = 3

osx.kivy_version = 1.9.1

fullscreen = 0

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CAMERA

android.api = 33

android.minapi = 21

android.ndk = 25b

android.accept_sdk_license = True

#android.bootstrap = sdl2
p4a.bootstrap = sdl2

android.entrypoint = org.kivy.android.PythonActivity

android.build_tools = 33.0.2

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]

log_level = 2

warn_on_root = 1
