[app]
title = WG Lite
package.name = wglite
package.domain = org.example

source.include_exts = py
requirements = python3,kivy,jnius

android.api = 30
android.minapi = 24
android.permissions = INTERNET

android.services = vpnservice:foreground

orientation = portrait
fullscreen = 0
