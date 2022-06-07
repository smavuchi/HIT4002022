package com.tinkertech.shop;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.json.JSONObject;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class NewAccountActivity extends AppCompatActivity {


    private EditText nameText, surnameText, growerIDText, password1Text, password2Text;
    private Button newAccountButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_account);

        nameText = findViewById(R.id.name);
        surnameText = findViewById(R.id.surname);
        growerIDText = findViewById(R.id.grower_id);
        password1Text = findViewById(R.id.password1);
        password2Text = findViewById(R.id.password2);
        newAccountButton = findViewById(R.id.new_account_button);


        newAccountButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                    FirebaseDatabase.getInstance().getReference("GrowerAccounts").child(growerIDText.getText().toString()).addValueEventListener(new ValueEventListener() {
                        @Override
                        public void onDataChange(@NonNull DataSnapshot snapshot) {
                            try {
                                if (snapshot.getValue() == null) {
                                    if (validateUserInputs()) {

                                        FirebaseDatabase.getInstance().
                                                getReference("GrowerAccounts").
                                                child(growerIDText.getText().toString()).
                                                child("name").setValue(nameText.getText().toString());

                                        FirebaseDatabase.getInstance().
                                                getReference("GrowerAccounts").
                                                child(growerIDText.getText().toString()).
                                                child("surname").setValue(surnameText.getText().toString());

                                        FirebaseDatabase.getInstance().
                                                getReference("GrowerAccounts").
                                                child(growerIDText.getText().toString()).
                                                child("password").setValue(password1Text.getText().toString());


                                        FirebaseDatabase.getInstance().getReference("GrowerAccounts").child(growerIDText.getText().toString()).removeEventListener(this);

                                        Toast.makeText(getApplicationContext(), "Account Created", Toast.LENGTH_SHORT).show();
                                        finish();
                                    } else {
                                        Toast.makeText(getApplicationContext(), "Invalid User Inputs", Toast.LENGTH_SHORT).show();
                                    }
                                } else {
                                    Toast.makeText(getApplicationContext(), "Account Exists", Toast.LENGTH_SHORT).show();

                                }
                            }catch (Exception e){
                                Toast.makeText(getApplicationContext(), "Internal App Error", Toast.LENGTH_SHORT).show();
                                e.printStackTrace();
                            }
                        }

                        @Override
                        public void onCancelled(@NonNull DatabaseError error) {

                        }
                    });

            }
        });

    }

    private boolean validateUserInputs() {
        return nameText.getText().toString().length() > 2 &&
                surnameText.getText().toString().length() > 2 &&
                parseGrowerNumber() &&
                password1Text.getText().toString().equals(password2Text.getText().toString()) &&
                password1Text.getText().toString().length() > 7 && password2Text.getText().toString().length() > 7;
    }

    private boolean parseGrowerNumber() {

        try {
            if (growerIDText.getText().toString().split("V")[1].length() == 6  && growerIDText.getText().toString().toCharArray()[0] == 'V') {
                Integer.parseInt(growerIDText.getText().toString().split("V")[1]);
                return true;
            }else{
                Toast.makeText(getApplicationContext(), "Invalid Grower ID", Toast.LENGTH_SHORT).show();
            }
        }catch (Exception e){
            Toast.makeText(getApplicationContext(), "Error Parsing Grower ID", Toast.LENGTH_SHORT).show();
            e.printStackTrace();
            return false;
        }

        return false;
    }

}
