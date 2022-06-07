package com.tinkertech.shop;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

public class MenuActivity extends AppCompatActivity {

    private String growerId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        ImageView orderingButton = findViewById(R.id.place_order);
        ImageView processedOrdersButton = findViewById(R.id.processed);
        ImageView rejectedOrdersButton = findViewById(R.id.rejected);
        final Resources codes = new Resources();

        growerId = getIntent().getStringExtra("gid");

        orderingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent categoryMenuIntent = new Intent(getApplicationContext(), CatalogActivity.class);
                categoryMenuIntent.putExtra("code", codes.OPTION_1_CODE);
                categoryMenuIntent.putExtra("gid", growerId);
                categoryMenuIntent.putExtra("action", "Orders");
                startActivity(categoryMenuIntent);
            }
        });


        processedOrdersButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent categoryMenuIntent = new Intent(getApplicationContext(), CatalogActivity.class);
                categoryMenuIntent.putExtra("code", codes.OPTION_3_CODE);
                categoryMenuIntent.putExtra("gid", growerId);
                categoryMenuIntent.putExtra("action", "ProcessedOrders");
                startActivity(categoryMenuIntent);
            }
        });

        rejectedOrdersButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent categoryMenuIntent = new Intent(getApplicationContext(), CatalogActivity.class);
                categoryMenuIntent.putExtra("code", codes.OPTION_2_CODE);
                categoryMenuIntent.putExtra("gid", growerId);
                categoryMenuIntent.putExtra("action", "RejectedOrders");
                startActivity(categoryMenuIntent);
            }
        });
    }
}
