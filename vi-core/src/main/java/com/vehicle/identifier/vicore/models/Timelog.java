package com.vehicle.identifier.vicore.models;

import javax.persistence.Entity;
import javax.persistence.Table;
import java.time.ZonedDateTime;

@Entity
@Table(name = "timelog")
public class Timelog extends Base{
    public ZonedDateTime loggedIn;
    public ZonedDateTime loggedOut;
    public String vehicleId;
    public String licensePlate;
    public String purposeOfVisit;

    public ZonedDateTime getLoggedIn() {
        return loggedIn;
    }

    public void setLoggedIn(ZonedDateTime loggedIn) {
        this.loggedIn = loggedIn;
    }

    public ZonedDateTime getLoggedOut() {
        return loggedOut;
    }

    public void setLoggedOut(ZonedDateTime loggedOut) {
        this.loggedOut = loggedOut;
    }

    public String getVehicleId() {
        return vehicleId;
    }

    public void setVehicleId(String vehicleId) {
        this.vehicleId = vehicleId;
    }

    public String getLicensePlate() {
        return licensePlate;
    }

    public void setLicensePlate(String licensePlate) {
        this.licensePlate = licensePlate;
    }

    public String getPurposeOfVisit() {
        return purposeOfVisit;
    }

    public void setPurposeOfVisit(String purposeOfVisit) {
        this.purposeOfVisit = purposeOfVisit;
    }
}