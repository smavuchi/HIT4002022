package com.tinkertech.admin;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.squareup.picasso.Picasso;

import java.util.Locale;

public class AnalyticsActivity extends AppCompatActivity {

  private int rejectedOrdersCounter=0, pendingOrdersCounter=0, processedOrdersCounter=0;
  private Message signalMessage;
  private Handler handler;

  private Thread signalingThread = new Thread(new Runnable() {
    @Override
    public void run() {
      while (true){
        try{
          signalMessage = new Message();
          signalMessage.obj = "RENDER GRAPH";
          handler.sendMessage(signalMessage);
          Thread.sleep(100);
        }catch (Exception e){
          e.printStackTrace();
        }
      }
    }
  });

  private ValueEventListener rejectedOrdersCountListener = new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot snapshot) {
      rejectedOrdersCounter = 0;
      try {
        for (DataSnapshot growers : snapshot.getChildren()) {
          for(DataSnapshot ds: growers.getChildren()){
            rejectedOrdersCounter++;
          }
        }

        rejectedOrdersCountText.setText(String.format(Locale.ENGLISH, "Rejected Orders: %d Bales",  rejectedOrdersCounter));
        rejectedOrdersCountText.setTextColor(0xffff0000);

      }catch (Exception e){
        e.printStackTrace();
        Toast.makeText(getApplicationContext(),"Internal App Error",Toast.LENGTH_SHORT).show();
      }
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {

    }
  };

  private ValueEventListener pendingOrdersCountListener = new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot snapshot) {
      pendingOrdersCounter = 0;
      try {
        for (DataSnapshot growers : snapshot.getChildren()) {
          for(DataSnapshot ds: growers.getChildren()){
            pendingOrdersCounter++;
          }
        }

        pendingOrdersCountText.setText(String.format(Locale.ENGLISH, "Pending Orders: %d Bales", pendingOrdersCounter));
      }catch (Exception e){
        e.printStackTrace();
        Toast.makeText(getApplicationContext(),"Internal App Error",Toast.LENGTH_SHORT).show();
      }
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {

    }
  };

  private ValueEventListener processedOrdersCountListener = new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot snapshot) {
      processedOrdersCounter = 0;
      try {
        for (DataSnapshot growers : snapshot.getChildren()) {
          for(DataSnapshot ds: growers.getChildren()){
            processedOrdersCounter++;
          }
        }

        processedOrdersCountText.setText(String.format(Locale.ENGLISH, "Processed Orders: %d Bales", processedOrdersCounter));
        processedOrdersCountText.setTextColor(0xff00ff00);
      }catch (Exception e){
        e.printStackTrace();
        Toast.makeText(getApplicationContext(),"Internal App Error",Toast.LENGTH_SHORT).show();
      }
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {

    }
  };

  private TextView pendingOrdersCountText, processedOrdersCountText, rejectedOrdersCountText;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_analytics);

    final ImageView outputChartView = findViewById(R.id.graph_output);

    handler = new Handler(Looper.getMainLooper()){
      @Override
      public void handleMessage(Message message){
        try {
          Picasso.get().load(String.format(Locale.ENGLISH, "https://plot-pp.herokuapp.com/plot?p1=%d&p2=%d&p3=%d", pendingOrdersCounter, processedOrdersCounter, rejectedOrdersCounter)).into(outputChartView);
        }catch (Exception e){
          Toast.makeText(getApplicationContext(), "Failed Chart Render", Toast.LENGTH_SHORT).show();
        }
      }

    };

    DatabaseReference pendingOrdersListener = FirebaseDatabase.getInstance().getReference("PendingOrders");
    DatabaseReference processedOrdersListener =  FirebaseDatabase.getInstance().getReference("ProcessedOrders");
    DatabaseReference rejectedOrdersListener =  FirebaseDatabase.getInstance().getReference("RejectedOrders");

    pendingOrdersCountText = findViewById(R.id.pending_orders_count);
    processedOrdersCountText = findViewById(R.id.processed_orders_count);
    rejectedOrdersCountText = findViewById(R.id.rejected_orders_count);

    pendingOrdersListener.addValueEventListener(pendingOrdersCountListener);
    processedOrdersListener.addValueEventListener(processedOrdersCountListener);
    rejectedOrdersListener.addValueEventListener(rejectedOrdersCountListener);

    signalingThread.start();
  }
}
