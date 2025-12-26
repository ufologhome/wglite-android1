[app]
title = WG Lite
package.name = wglite
package.domain = org.example

source.include_exts = py
requirements = python3,kivy,jnius

android.api = 25
android.minapi = 24
android.permissions = INTERNET

android.services = vpnservice:foreground

orientation = portrait
fullscreen = 0

android.manifest.application_args = \
    <service android:name="org.kivy.android.PythonService" \
    android:permission="android.permission.BIND_VPN_SERVICE" \
    android:exported="true"> \
        <intent-filter> \
            <action android:name="android.net.VpnService"/> \
        </intent-filter> \
    </service>
