[app]
title = WG Lite
package.name = wglite
package.domain = org.example

# ГДЕ КОД
source.dir = .
source.include_exts = py

# ВЕРСИЯ (ОБЯЗАТЕЛЬНО)
version = 0.1

# ЗАВИСИМОСТИ
requirements = python3,kivy,pyjnius

# ANDROID 7.1.2
android.api = 25
android.minapi = 24
android.build_tools = 30.0.3

# ПРАВА
android.permissions = INTERNET

# VPN service
android.services = vpnservice:foreground

# UI
orientation = portrait
fullscreen = 0

# VPN SERVICE В MANIFEST
android.manifest.application_args = \
    <service android:name="org.kivy.android.PythonService" \
    android:permission="android.permission.BIND_VPN_SERVICE" \
    android:exported="true"> \
        <intent-filter> \
            <action android:name="android.net.VpnService"/> \
        </intent-filter> \
    </service>
