package com.tinkertech.shop;


import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.Locale;


public class ObjectAdapter extends RecyclerView.Adapter<ObjectAdapter.ViewHolder> {

    private ArrayList<Item> dataSetObject;
    private CatalogActivity catalogActivity;
    private boolean enableEdit = false;

    ObjectAdapter(ArrayList<Item> data, CatalogActivity catalogActivity){
        dataSetObject = data;
        this.catalogActivity = catalogActivity;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_card_view,parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, final int position) {

        final TextView statusTextView = holder.headerTextView;
        final TextView processItemTextView = holder.editItemTextView;
        final TextView gidTextView = holder.gidTextView;
        final TextView quantityTextView = holder.quantityTextView;
        final TextView gradeTextView = holder.gradeTextView;
        final ImageView sampleImageView = holder.sampleImageView;
        final ImageView removeItemButton = holder.removeItemButton;

        switch (catalogActivity.action){

            case "RejectedOrders":
                statusTextView.setTextColor(0xffff0000);
                removeItemButton.setVisibility(View.GONE);
                processItemTextView.setVisibility(View.GONE);
                gradeTextView.setText("GRADE");
                gidTextView.setText(dataSetObject.get(position).getGrade());
                gidTextView.setTextColor(0xffff0000);
                break;

            case "ProcessedOrders":
                gradeTextView.setText("GRADE");
                statusTextView.setTextColor(0xff00ff00);
                removeItemButton.setVisibility(View.GONE);
                processItemTextView.setVisibility(View.GONE);
                gidTextView.setText(dataSetObject.get(position).getGrade());
                break;

            default:
                gidTextView.setText(dataSetObject.get(position).getSourceID());
                break;
        }

        statusTextView.setText(dataSetObject.get(position).getStatus());
        quantityTextView.setText(String.format(Locale.ENGLISH,"%d",dataSetObject.get(position).getQuantity()));
        sampleImageView.setImageResource(R.mipmap.item);
        sampleImageView.setEnabled(false);

        removeItemButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String id = dataSetObject.get(position).generateObjectId().getObjectId();
                catalogActivity.removeObject(id, position);
                Toast.makeText(catalogActivity.getApplicationContext(), "Item Removed", Toast.LENGTH_SHORT).show();
            }
        });

        processItemTextView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if(enableEdit) {
                    Toast.makeText(catalogActivity.getApplicationContext(), "Edit Disabled", Toast.LENGTH_SHORT).show();
                    statusTextView.setEnabled(false);
                    gidTextView.setEnabled(false);
                    sampleImageView.setEnabled(false);
                    quantityTextView.setEnabled(false);
                    enableEdit = false;

                    String name = statusTextView.getText().toString();
                    String gid =  gidTextView.getText().toString();
                    int quantity = Integer.parseInt(quantityTextView.getText().toString());
                    catalogActivity.insertObject(name, gid, quantity, dataSetObject.get(position));
                    processItemTextView.setText("Edit Item");

                }else{
                    Toast.makeText(catalogActivity.getApplicationContext(), "Edit Enabled", Toast.LENGTH_SHORT).show();
                    processItemTextView.setText("Save Item");
                    statusTextView.setEnabled(true);
                    gidTextView.setEnabled(true);
                    sampleImageView.setEnabled(true);
                    quantityTextView.setEnabled(true);
                    enableEdit = true;
                }
            }
        });

    }

    @Override
    public int getItemCount() {
        return dataSetObject.size();
    }

    class ViewHolder extends RecyclerView.ViewHolder {

        TextView headerTextView;
        TextView editItemTextView;
        TextView gidTextView;
        TextView quantityTextView;
        TextView gradeTextView;
        ImageView sampleImageView;
        ImageView removeItemButton;

        ViewHolder(@NonNull View itemView) {
            super(itemView);

            gradeTextView = itemView.findViewById(R.id.gradeLabel);
            headerTextView = itemView.findViewById(R.id.item_status);
            editItemTextView = itemView.findViewById(R.id.edit_item);
            gidTextView = itemView.findViewById(R.id.sourceID);
            sampleImageView = itemView.findViewById(R.id.sample_image);
            removeItemButton = itemView.findViewById(R.id.remove_item);
            quantityTextView = itemView.findViewById(R.id.quantity_text);

        }
    }
}
