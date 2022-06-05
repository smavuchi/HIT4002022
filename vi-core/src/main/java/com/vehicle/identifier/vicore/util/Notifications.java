package com.vehicle.identifier.vicore.util;

import com.vehicle.identifier.vicore.model.Driver;
import com.vehicle.identifier.vicore.model.Notification;
import com.vehicle.identifier.vicore.model.TimeLog;
import com.vehicle.identifier.vicore.model.Vehicle;

import static com.vehicle.identifier.vicore.util.Util.currentTime;
import static com.vehicle.identifier.vicore.util.Util.uuid;

public class Notifications {

    static Notification notification = new Notification();

    public static Notification arrivalNotification(TimeLog timeLog, Driver driver){

        String message = "Good day" + driver.getFirstname() + driver.getLastname() +
                "<br /> Welcome to Harare Institute of Technology <br /> Your entry time is:" +
                timeLog.getEntered();

        notification.setId(uuid());
        notification.setCreated(currentTime());
        notification.setUpdated(currentTime());
        notification.setDestination(driver.getMsisdn());
        notification.setMessage(message);

        return notification;
    }

    public Notification depatureNotification(Notification notification){


        return notification;
    }

    public static Notification registrationNotification(Vehicle vehicle){
        String message = "Good day Admin" +
                "<br /> New a new vehicle with license plate" + vehicle.getLicensePlate() +
                "has been added to the database. " +
                "Please add driver details to the associated vehicle on the following URL " +
                "<br /> localhost:8080/register/driver";

        notification.setId(uuid());
        notification.setCreated(currentTime());
        notification.setUpdated(currentTime());
        notification.setDestination("vimurungu@gmail.com");
        notification.setMessage(message);
        return notification;
    }

    public Notification updateNotification(Notification notification){

        return notification;
    }
}
