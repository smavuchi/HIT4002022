package com.tinkertech.shop;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.DefaultItemAnimator;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.Locale;

public class CatalogActivity extends AppCompatActivity {

    private ArrayList<Item> data;
    private ObjectAdapter objectAdapter;
    private RecyclerView itemRecyclerView;
    private LinearLayoutManager recyclerLayoutManager;
    private DatabaseReference stockDatabaseRef;
    public Resources resources;
    private TextView categoryTextView;

    private final int OPTION_1_CODE =   0xff000000;
    private final int OPTION_2_CODE =   0xff000001;
    private final int OPTION_3_CODE =   0xff000002;
    private int currentCategoryCode;
    private String growerID, selector, selectorHeading;
    private final int MAXIMUM_ORDER_LIMIT = 5;
    private long count = 0;
    public String action;

    private ValueEventListener databaseObjectHandler = new ValueEventListener() {
        @Override
        public void onDataChange(@NonNull DataSnapshot snapshot) {
            try {
                data.clear();
                itemRecyclerView.setAdapter(objectAdapter);
                count = snapshot.getChildrenCount();
                categoryTextView.setText(String.format(Locale.ENGLISH, "%s: %d", selectorHeading, count));
                for (DataSnapshot ds : snapshot.getChildren()) {
                    Item item = new Item(
                            ds.child("status").getValue(String.class),
                            ds.child("sourceID").getValue(String.class),
                            ds.child("quantity").getValue(Integer.class),
                            ds.child("grade").getValue(String.class)
                    );
                    data.add(item);
                }
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
        ImageView addItemButton = findViewById(R.id.add_item);
        categoryTextView = findViewById(R.id.category_text);


        currentCategoryCode = getIntent().getIntExtra("code",0);getIntent().getIntExtra("code",0);
        growerID = getIntent().getStringExtra("gid");
        action = getIntent().getStringExtra("action");

        addItemButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(MAXIMUM_ORDER_LIMIT > count) {
                    data.add(new Item(getString(R.string.status), growerID, 1, "").generateObjectId());
                    itemRecyclerView.setAdapter(objectAdapter);
                    Toast.makeText(getApplicationContext(), "New Order", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(getApplicationContext(),"Limit Exceeded",Toast.LENGTH_SHORT).show();
                }
            }
        });


        switch (currentCategoryCode){

            case OPTION_1_CODE:
                categoryTextView.setText(R.string.label_1);
                iconView.setImageResource(R.mipmap.place);
                selector = "PendingOrders";
                selectorHeading = "Pending Orders";
                break;

            case OPTION_2_CODE:
                categoryTextView.setText(R.string.label_5);
                iconView.setImageResource(R.mipmap.rejected);
                addItemButton.setVisibility(View.INVISIBLE);
                selector = "RejectedOrders";
                selectorHeading = "Rejected Orders";
                break;

            case OPTION_3_CODE:
                categoryTextView.setText(R.string.label_1);
                iconView.setImageResource(R.mipmap.place);
                addItemButton.setVisibility(View.INVISIBLE);
                selector = "ProcessedOrders";
                selectorHeading = "Processed Orders";
                break;

            default:
                finish();

        }

        stockDatabaseRef =  FirebaseDatabase.getInstance().getReference(selector).child(growerID);
        stockDatabaseRef.addValueEventListener(databaseObjectHandler);

    }


    public void insertObject(String status, String growerIDString, int quantity, Item item) {
        try {

            item.generateObjectId();
            FirebaseDatabase.getInstance().getReference(resources.STOCK_REF).child(growerID).child(item.getObjectId()).removeValue();
            item.setStatus(status);
            item.setSourceID(growerIDString);
            item.setQuantity(quantity);
            item.generateObjectId();

            data.clear();
            itemRecyclerView.setAdapter(objectAdapter);
            item.generateObjectId();
            stockDatabaseRef.child(item.getObjectId()).setValue(item)
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

    public void removeObject(String id, int index) {
        stockDatabaseRef.child(id).removeValue();
        data.remove(index);
        itemRecyclerView.setAdapter(objectAdapter);
    }
}
