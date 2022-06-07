package com.tinkertech.admin;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

public class MenuActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        ImageView orderingButton = findViewById(R.id.place_order);
        ImageView processedButton = findViewById(R.id.processed);
        ImageView rejectedButton = findViewById(R.id.rejected);
        ImageView userLogoutButton = findViewById(R.id.exit_app);
        ImageView analyticsButton = findViewById(R.id.view_analysis);
        ImageView settingsButton = findViewById(R.id.settings);

        final Resources codes = new Resources();


        orderingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent categoryMenuIntent = new Intent(getApplicationContext(), CatalogActivity.class);
                categoryMenuIntent.putExtra("code", codes.OPTION_1_CODE);
                categoryMenuIntent.putExtra("action", "Orders");
                startActivity(categoryMenuIntent);
            }
        });


        rejectedButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent categoryMenuIntent = new Intent(getApplicationContext(), CatalogActivity.class);
                categoryMenuIntent.putExtra("code", codes.OPTION_2_CODE);
                categoryMenuIntent.putExtra("action", "RejectedOrders");
                startActivity(categoryMenuIntent);
            }
        });

        processedButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent categoryMenuIntent = new Intent(getApplicationContext(), CatalogActivity.class);
                categoryMenuIntent.putExtra("code", codes.OPTION_3_CODE);
                categoryMenuIntent.putExtra("action", "ProcessedOrders");
                startActivity(categoryMenuIntent);
            }
        });


        settingsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent settingsIntent = new Intent(getApplicationContext(), SettingsActivity.class);
                startActivity(settingsIntent);
            }
        });

        analyticsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), AnalyticsActivity.class));
            }
        });

        userLogoutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
