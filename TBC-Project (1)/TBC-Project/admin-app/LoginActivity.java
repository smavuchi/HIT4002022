package com.tinkertech.admin;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;


public class LoginActivity extends AppCompatActivity {

  private EditText emailAddress;
  private  EditText password;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_login);

    emailAddress = findViewById(R.id.grower_id);
    password = findViewById(R.id.password);
    final ProgressBar progressBar = findViewById(R.id.progress);

    Button loginButton = findViewById(R.id.login_button);

    loginButton.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View v) {
        progressBar.setVisibility(View.VISIBLE);
        try {
          FirebaseAuth.getInstance().signInWithEmailAndPassword(emailAddress.getText().toString(), password.getText().toString()).addOnSuccessListener(new OnSuccessListener<AuthResult>() {
            @Override
            public void onSuccess(AuthResult authResult) {
              progressBar.setVisibility(View.GONE);
              startActivity(new Intent(getApplicationContext(), MenuActivity.class));
              finish();
            }
          }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
              progressBar.setVisibility(View.GONE);
              Toast.makeText(getApplicationContext(), "Login Failed", Toast.LENGTH_SHORT).show();
            }
          });
        }catch (Exception e){
          progressBar.setVisibility(View.GONE);
        }
      }
    });

  }

}
