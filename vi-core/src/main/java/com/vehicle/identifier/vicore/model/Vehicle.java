package com.vehicle.identifier.vicore.model;

import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "vehicle")
public class Vehicle extends Base{
    private String color;
    private String make;
    private String model;
    private String licensePlate;
    private String licensePlateNationality;
    private String driverId;
    private boolean blacklisted;

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getMake() {
        return make;
    }

    public void setMake(String make) {
        this.make = make;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getLicensePlate() {
        return licensePlate;
    }

    public void setLicensePlate(String licensePlate) {
        this.licensePlate = licensePlate;
    }

    public String getLicensePlateNationality() {
        return licensePlateNationality;
    }

    public void setLicensePlateNationality(String licensePlateNationality) {
        this.licensePlateNationality = licensePlateNationality;
    }

    public String getDriverId() {
        return driverId;
    }

    public void setDriverId(String driverId) {
        this.driverId = driverId;
    }

    public boolean isBlacklisted() {
        return blacklisted;
    }

    public void setBlacklisted(boolean blacklisted) {
        this.blacklisted = blacklisted;
    }
}
