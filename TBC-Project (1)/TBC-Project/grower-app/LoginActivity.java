package com.tinkertech.shop;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;


public class LoginActivity extends AppCompatActivity {

    private EditText growerNumberText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        growerNumberText = findViewById(R.id.grower_id);
        final EditText password = findViewById(R.id.password);
        final ProgressBar progressBar = findViewById(R.id.progress);
        Button loginButton = findViewById(R.id.login_button);
        TextView newAccountLabel = findViewById(R.id.new_account);

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(parseGrowerNumber()) {
                    FirebaseDatabase.getInstance().getReference("GrowerAccounts").child(growerNumberText.getText().toString()).addValueEventListener(new ValueEventListener() {
                        @Override
                        public void onDataChange(@NonNull DataSnapshot snapshot) {
                            try{
                                if(password.getText().toString().equals(snapshot.child("password").getValue(String.class))){
                                    Intent i = new Intent(getApplicationContext(), MenuActivity.class);
                                    i.putExtra("gid", growerNumberText.getText().toString());
                                    startActivity(i);
                                    finish();
                                }else{
                                    Toast.makeText(getApplicationContext(), "Invalid Grower ID or Password", Toast.LENGTH_SHORT).show();
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
                }else{
                    Toast.makeText(getApplicationContext(), "Invalid Grower ID", Toast.LENGTH_SHORT).show();
                }
            }
        });



        newAccountLabel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), NewAccountActivity.class));
            }
        });
    }

    private boolean parseGrowerNumber() {

        try {
            if (growerNumberText.getText().toString().split("V")[1].length() == 6  && growerNumberText.getText().toString().toCharArray()[0] == 'V') {
                Integer.parseInt(growerNumberText.getText().toString().split("V")[1]);
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
