package com.tinkertech.shop;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

public class SplashActivity extends AppCompatActivity {

    private Thread startupThread = new Thread(new Runnable() {
        @Override
        public void run() {

            try{
                Thread.sleep(2000);
                startActivity(new Intent(getApplicationContext(), LoginActivity.class));
                finish();
            }catch(Exception ignored){ }

        }
    });


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        startupThread.start();

    }
}
