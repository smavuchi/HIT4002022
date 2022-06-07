package com.vehicle.identifier.vicore.models;

import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "notification")
public class Notification extends Base{
    private String  type;
    private String  destination;
    private String  message;

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
