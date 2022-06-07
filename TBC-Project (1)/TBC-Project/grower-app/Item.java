package com.tinkertech.shop;

public class Item {
    private String status;
    private String sourceID;
    private String objectId;
    private String grade;
    private int quantity;

    public Item(String status, String sourceID, int quantity, String grade){
        this.status = status;
        this.sourceID = sourceID;
        this.quantity = quantity;
        this.grade = grade;
    }


    public Item generateObjectId() {
        this.objectId = new Hash().getSHA256(sourceID + quantity +"");
        return this;
    }

    public String getObjectId() {
        return objectId;
    }

    public String getStatus() {
        return status;
    }

    public String getSourceID() { return sourceID; }

    public int getQuantity() { return quantity; }

    public void setStatus(String status) {
        this.status = status;
    }

    public void setSourceID(String sourceID) {
        this.sourceID = sourceID;
    }

    public void setQuantity(int quantity) { this.quantity = quantity; }

    public String getGrade() { return grade; }
}
