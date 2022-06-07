package com.tinkertech.admin;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.Locale;

public class SettingsActivity extends AppCompatActivity {

    private DatabaseReference settingsRef;
    private EditText getXLText, getXFText, getCLText, getCFText, getBLText, getBFText, getBRText;

    private ValueEventListener settingsEventListener = new ValueEventListener() {
        @Override
        public void onDataChange(@NonNull DataSnapshot snapshot) {
            try{
                getXLText.setText(String.format(Locale.ENGLISH ,"%f", snapshot.child("XL").getValue(Double.class)));
                getXFText.setText(String.format(Locale.ENGLISH ,"%f", snapshot.child("XF").getValue(Double.class)));
                getCLText.setText(String.format(Locale.ENGLISH ,"%f", snapshot.child("CL").getValue(Double.class)));
                getCFText.setText(String.format(Locale.ENGLISH ,"%f", snapshot.child("CF").getValue(Double.class)));
                getBLText.setText(String.format(Locale.ENGLISH ,"%f", snapshot.child("BL").getValue(Double.class)));
                getBFText.setText(String.format(Locale.ENGLISH ,"%f", snapshot.child("BF").getValue(Double.class)));
                getBRText.setText(String.format(Locale.ENGLISH ,"%f", snapshot.child("BR").getValue(Double.class)));
            }catch (Exception e){
                Toast.makeText(getApplicationContext(), "Load Error", Toast.LENGTH_SHORT).show();
                e.printStackTrace();
            }
        }

        @Override
        public void onCancelled(@NonNull DatabaseError error) {

        }
    };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        settingsRef = FirebaseDatabase.getInstance().getReference("settings");
        Button setXLButton = findViewById(R.id.set_xl);
        Button setXFButton = findViewById(R.id.set_xf);
        Button setCLButton = findViewById(R.id.set_cl);
        Button setCFButton = findViewById(R.id.set_cf);
        Button setBLButton = findViewById(R.id.set_bl);
        Button setBFButton = findViewById(R.id.set_bf);
        Button setBRButton = findViewById(R.id.set_br);

        getXLText = findViewById(R.id.grade_xl_peg);
        getXFText = findViewById(R.id.grade_xf_peg);
        getCLText = findViewById(R.id.grade_cl_peg);
        getCFText = findViewById(R.id.grade_cf_peg);
        getBLText = findViewById(R.id.grade_bl_peg);
        getBFText = findViewById(R.id.grade_bf_peg);
        getBRText = findViewById(R.id.grade_br_peg);

        settingsRef.addValueEventListener(settingsEventListener);
        setXLButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    settingsRef.child("XL").setValue(Double.parseDouble(getXLText.getText().toString()));
                    Toast.makeText(getApplicationContext(), "Setting Value", Toast.LENGTH_SHORT).show();
                }catch (Exception e){
                    Toast.makeText(getApplicationContext(), "Set Error", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }
        });

        setXFButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    settingsRef.child("XF").setValue(Double.parseDouble(getXFText.getText().toString()));
                    Toast.makeText(getApplicationContext(), "Setting Value", Toast.LENGTH_SHORT).show();
                }catch (Exception e){
                    Toast.makeText(getApplicationContext(), "Set Error", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }
        });

        setCLButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    settingsRef.child("CL").setValue(Double.parseDouble(getCLText.getText().toString()));
                    Toast.makeText(getApplicationContext(), "Setting Value", Toast.LENGTH_SHORT).show();
                }catch (Exception e){
                    Toast.makeText(getApplicationContext(), "Set Error", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }
        });

        setCFButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    settingsRef.child("CF").setValue(Double.parseDouble(getCFText.getText().toString()));
                    Toast.makeText(getApplicationContext(), "Setting Value", Toast.LENGTH_SHORT).show();
                }catch (Exception e){
                    Toast.makeText(getApplicationContext(), "Set Error", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }
        });

        setBLButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    settingsRef.child("BL").setValue(Double.parseDouble(getBLText.getText().toString()));
                    Toast.makeText(getApplicationContext(), "Setting Value", Toast.LENGTH_SHORT).show();
                }catch (Exception e){
                    Toast.makeText(getApplicationContext(), "Set Error", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }
        });

        setBFButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    settingsRef.child("BF").setValue(Double.parseDouble(getBFText.getText().toString()));
                    Toast.makeText(getApplicationContext(), "Setting Value", Toast.LENGTH_SHORT).show();
                }catch (Exception e){
                    Toast.makeText(getApplicationContext(), "Set Error", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }
        });

        setBRButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    settingsRef.child("BR").setValue(Double.parseDouble(getBRText.getText().toString()));
                    Toast.makeText(getApplicationContext(), "Setting Value", Toast.LENGTH_SHORT).show();
                }catch (Exception e){
                    Toast.makeText(getApplicationContext(), "Set Error", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }
        });
    }
}
