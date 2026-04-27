[app]
title = MyApp
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
