package com.tinkertech.admin;


import android.content.Intent;
import android.provider.MediaStore;
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
        final TextView gidTextView = holder.gidTextView;
        final TextView quantityTextView = holder.quantityTextView;
        final ImageView removeItemButton = holder.removeItemButton;

        statusTextView.setText(dataSetObject.get(position).getStatus());
        gidTextView.setText(dataSetObject.get(position).getSourceID());
        quantityTextView.setText(String.format(Locale.ENGLISH,"%d",dataSetObject.get(position).getQuantity()));

        switch (catalogActivity.action){

            case "RejectedOrders":
                statusTextView.setTextColor(0xffff0000);
                removeItemButton.setVisibility(View.GONE);
                holder.cameraButton.setVisibility(View.GONE);
                break;

            case "ProcessedOrders":
                statusTextView.setTextColor(0xff00ff00);
                removeItemButton.setVisibility(View.GONE);
                holder.cameraButton.setVisibility(View.GONE);
                break;
        }

        holder.cameraButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try{
                    catalogActivity.currentGID = dataSetObject.get(position).getSourceID();
                    catalogActivity.currentTarget = "ProcessedOrders";
                    dataSetObject.get(position).generateObjectId();
                    catalogActivity.currentObjectId = dataSetObject.get(position).getObjectId();
                    Intent getImageIntent = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.INTERNAL_CONTENT_URI);
                    catalogActivity.startActivityForResult(getImageIntent, CatalogActivity.REQUEST_IMAGE);
                }catch (Exception e){
                    e.printStackTrace();
                    Toast.makeText(catalogActivity.getApplicationContext(), "Operation Failed", Toast.LENGTH_SHORT).show();
                }
            }
        });

        removeItemButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                catalogActivity.insertObject("Rejected", dataSetObject.get(position).getSourceID(), "RejectedOrders",dataSetObject.get(position));
            }
        });

    }

    @Override
    public int getItemCount() {
        return dataSetObject.size();
    }

    class ViewHolder extends RecyclerView.ViewHolder {

        TextView headerTextView;
        TextView gidTextView;
        TextView quantityTextView;
        ImageView sampleImageView;
        ImageView removeItemButton;
        ImageView cameraButton;

        ViewHolder(@NonNull View itemView) {
            super(itemView);

            headerTextView = itemView.findViewById(R.id.item_status);
            gidTextView = itemView.findViewById(R.id.sourceID);
            sampleImageView = itemView.findViewById(R.id.sample_image);
            removeItemButton = itemView.findViewById(R.id.remove_item);
            quantityTextView = itemView.findViewById(R.id.quantity_text);
            cameraButton = itemView.findViewById(R.id.scan_item);

        }
    }
}
