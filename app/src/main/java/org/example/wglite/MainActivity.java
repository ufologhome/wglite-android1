package org.example.wglite;

import android.app.Activity;
import android.content.Intent;
import android.net.VpnService;
import android.os.Bundle;
import android.widget.Button;

public class MainActivity extends Activity {

    private static final int VPN_REQUEST = 1;
    private Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn = findViewById(R.id.btnVpn);

        btn.setOnClickListener(v -> {
            Intent intent = VpnService.prepare(this);
            if (intent != null) {
                startActivityForResult(intent, VPN_REQUEST);
            } else {
                startVpn();
            }
        });
    }

    private void startVpn() {
        startService(new Intent(this, MyVpnService.class));
        btn.setText("VPN: ON");
    }
}
