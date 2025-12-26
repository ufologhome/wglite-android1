from jnius import autoclass
from android import activity

PythonActivity = autoclass('org.kivy.android.PythonActivity')
VpnService = autoclass('android.net.VpnService')
Intent = autoclass('android.content.Intent')

def start_vpn():
    ctx = PythonActivity.mActivity
    intent = VpnService.prepare(ctx)
    if intent:
        ctx.startActivityForResult(intent, 0)
    else:
        _start_service()

def _start_service():
    ctx = PythonActivity.mActivity
    intent = Intent(ctx, autoclass('org.kivy.android.PythonService'))
    intent.putExtra("serviceClass", "vpnservice.MyVpnService")
    ctx.startService(intent)

def stop_vpn():
    ctx = PythonActivity.mActivity
    intent = Intent(ctx, autoclass('org.kivy.android.PythonService'))
    ctx.stopService(intent)

