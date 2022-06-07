package com.tinkertech.admin;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.DefaultItemAnimator;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.androidnetworking.AndroidNetworking;
import com.androidnetworking.error.ANError;
import com.androidnetworking.interfaces.StringRequestListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.UploadTask;

import java.util.ArrayList;
import java.util.Locale;
import java.util.Random;

public class CatalogActivity extends AppCompatActivity {

  public static final int REQUEST_IMAGE = 90 ;
  private ArrayList<Item> data;
  private ObjectAdapter objectAdapter;
  private RecyclerView itemRecyclerView;
  private LinearLayoutManager recyclerLayoutManager;
  private DatabaseReference stockDatabaseRef;
  public Resources resources;
  private TextView categoryTextView;

  public String currentTarget, currentGID, currentObjectId;

  private final int OPTION_1_CODE =   0xff000000;
  private final int OPTION_2_CODE =   0xff000001;
  private final int OPTION_3_CODE =   0xff000002;
  private int currentCategoryCode;
  private String  selectorHeading;
  public String selector;
  private long count = 0;
  private int rId = 0;
  public String action;

  private ValueEventListener databaseObjectHandler = new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot snapshot) {
      try {
        data.clear();
        itemRecyclerView.setAdapter(objectAdapter);
        count = 0;

        for (DataSnapshot mds : snapshot.getChildren()) {
          for( DataSnapshot ds : mds.getChildren()) {
            Item item = new Item(ds.child("status").getValue(String.class), ds.child("sourceID").getValue(String.class), ds.child("quantity").getValue(Integer.class));
            data.add(item);
            count++;
          }
        }

        categoryTextView.setText(String.format(Locale.ENGLISH, "%s: %d", selectorHeading, count));
        itemRecyclerView.setAdapter(objectAdapter);
      }catch (Exception e){
        e.printStackTrace();
        Toast.makeText(getApplicationContext(),"Internal App Error",Toast.LENGTH_SHORT).show();
      }
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {

    }
  };


  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_catalog);

    data = new ArrayList<>();
    resources = new Resources();
    objectAdapter = new ObjectAdapter(data, this);
    itemRecyclerView = findViewById(R.id.item_list);
    itemRecyclerView.setHasFixedSize(true);

    recyclerLayoutManager = new LinearLayoutManager(this);
    itemRecyclerView.setLayoutManager(recyclerLayoutManager);
    itemRecyclerView.setItemAnimator(new DefaultItemAnimator());
    itemRecyclerView.setAdapter(objectAdapter);

    ImageView iconView = findViewById(R.id.icon_symbol);
    categoryTextView = findViewById(R.id.category_text);


    currentCategoryCode = getIntent().getIntExtra("code",0);getIntent().getIntExtra("code",0);
    action = getIntent().getStringExtra("action");


    switch (currentCategoryCode){

      case OPTION_1_CODE:
        categoryTextView.setText(R.string.label_1);
        selector = "PendingOrders";
        selectorHeading = "Pending Orders";
        break;

      case OPTION_2_CODE:
        categoryTextView.setText(R.string.label_5);
        iconView.setImageResource(R.mipmap.rejected);
        selector = "RejectedOrders";
        selectorHeading = "Rejected Orders";
        break;

      case OPTION_3_CODE:
        categoryTextView.setText(R.string.label_1);
        selector = "ProcessedOrders";
        selectorHeading = "Processed Orders";
        break;

      default:
        finish();

    }

    stockDatabaseRef =  FirebaseDatabase.getInstance().getReference(selector);
    stockDatabaseRef.addValueEventListener(databaseObjectHandler);

  }


  public void insertObject(String status, String growerIDString, String target, Item item) {
    try {

      item.generateObjectId();
      FirebaseDatabase.getInstance().getReference(selector).child(growerIDString).child(item.getObjectId()).removeValue();
      item.setStatus(status);
      item.setSourceID(growerIDString);
      item.generateObjectId();

      data.clear();
      itemRecyclerView.setAdapter(objectAdapter);
      item.generateObjectId();
      FirebaseDatabase.getInstance().getReference(target).child(growerIDString).child(item.getObjectId()).setValue(item)
              .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(Void aVoid) {
                  Toast.makeText(getApplicationContext(),"Queued",Toast.LENGTH_SHORT).show();
                }
              }).addOnFailureListener(new OnFailureListener() {
        @Override
        public void onFailure(@NonNull Exception e) {
          Toast.makeText(getApplicationContext(),"Queueing Failed",Toast.LENGTH_SHORT).show();
        }
      });

    }catch (Exception e){
      Toast.makeText(getApplicationContext(),e.toString(),Toast.LENGTH_SHORT).show();
    }
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
      if(resultCode == RESULT_OK && requestCode == REQUEST_IMAGE){
        uploadNewImage(data.getData());
        Toast.makeText(getApplicationContext(),"Uploading",Toast.LENGTH_SHORT).show();
      }else{
        Toast.makeText(getApplicationContext(),"Null",Toast.LENGTH_SHORT).show();
      }
  }

  private void uploadNewImage(Uri imageUri) {

    try {
      FirebaseStorage.getInstance().getReference()
              .child(currentTarget).child(currentGID)
              .child(currentObjectId).putFile(imageUri).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
        @Override
        public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
          rId = new Random().nextInt();
          FirebaseDatabase.getInstance().getReference("OrderQueue").child("QueuedTasks").child(currentGID+":"+currentObjectId).setValue("PENDING SCAN");
          Toast.makeText(getApplicationContext(), "Image Saved", Toast.LENGTH_SHORT).show();
        }
      }).addOnFailureListener(new OnFailureListener() {
        @Override
        public void onFailure(@NonNull Exception e) {
          Toast.makeText(getApplicationContext(), "Image Upload Failed", Toast.LENGTH_SHORT).show();
        }
      });

    }catch (Exception e){
      Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_SHORT).show();
    }

  }
}
