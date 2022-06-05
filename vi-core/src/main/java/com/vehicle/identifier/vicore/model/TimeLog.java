package com.vehicle.identifier.vicore.model;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.time.ZonedDateTime;

@Entity
@Table(name = "timeLog")
public class TimeLog extends Base{
    private ZonedDateTime entered;
    private ZonedDateTime exited;
    private String vehicleId;
    private String purposeOfVisit;

    public ZonedDateTime getEntered() {
        return entered;
    }

    public void setEntered(ZonedDateTime entered) {
        this.entered = entered;
    }

    public ZonedDateTime getExited() {
        return exited;
    }

    public void setExited(ZonedDateTime exited) {
        this.exited = exited;
    }

    public String getVehicleId() {
        return vehicleId;
    }

    public void setVehicleId(String vehicleId) {
        this.vehicleId = vehicleId;
    }

    public String getPurposeOfVisit() {
        return purposeOfVisit;
    }

    public void setPurposeOfVisit(String purposeOfVisit) {
        this.purposeOfVisit = purposeOfVisit;
    }
}
