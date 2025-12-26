from jnius import autoclass, PythonJavaClass, java_method
from android import activity
import threading

PythonActivity = autoclass('org.kivy.android.PythonActivity')
VpnService = autoclass('android.net.VpnService')
Intent = autoclass('android.content.Intent')

SERVER_IP = "192.168.0.150"
SERVER_PORT = 51820


# ===== LAUNCHER =====

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


# ===== VPN SERVICE =====

class MyVpnService(PythonJavaClass):
    __javabase__ = 'android/net/VpnService'

    @java_method('()V')
    def onCreate(self):
        builder = self.Builder()
        builder.addAddress("10.0.0.2", 32)
        builder.addRoute("0.0.0.0", 0)
        builder.setMtu(1400)

        pfd = builder.establish()
        tun_fd = pfd.detachFd()

        from tunloop import tun_loop
        from udploop import udp_loop

        threading.Thread(
            target=tun_loop,
            args=(tun_fd, SERVER_IP, SERVER_PORT),
            daemon=True
        ).start()

        threading.Thread(
            target=udp_loop,
            args=(tun_fd,),
            daemon=True
        ).start()
