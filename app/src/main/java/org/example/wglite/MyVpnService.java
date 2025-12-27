package org.example.wglite;

import android.net.VpnService;
import android.os.ParcelFileDescriptor;

public class MyVpnService extends VpnService {

    private ParcelFileDescriptor tun;

    @Override
    public void onCreate() {
        super.onCreate();

        Builder builder = new Builder();
        builder.setSession("WG Lite");
        builder.addAddress("10.0.0.2", 32);
        builder.addRoute("0.0.0.0", 0);

        tun = builder.establish();
    }
}
