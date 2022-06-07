package com.vehicle.identifier.vicore.util;

import com.vehicle.identifier.vicore.models.Driver;
import com.vehicle.identifier.vicore.models.Notification;
import com.vehicle.identifier.vicore.models.Timelog;
import com.vehicle.identifier.vicore.models.Vehicle;

public class Notifications {

    public static Notification registration(Driver driver){

        String message = "Good day,<br>" +
                "Thanks for interest in registering onto the HIT Gate system.<br>" +
                "We expect your next gate entry to be seamless.";

        Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setDestination(driver.getEmail());
        notification.setType("HIT Gate System Registration");
        notification.setMessage(message);

        return notification;
    }

    public static Notification unverifiedDriver(Timelog timeLog, Vehicle vehicle){

        String message = "Good day Admin" +
                "<br> Vehicle with reg number is "+ vehicle.getLicensePlate() +
                " is attempting entry once again without registration.<br>" +
                "If you get this alert again, please consider blocking this vehicle.<br>" +
                "Attempt entry time is:" +
                timeLog.getLoggedIn() + "<br>";

        Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setDestination("h170198q@hit.ac.zw");
        notification.setType("Security Alert");
        notification.setMessage(message);

        return notification;
    }

    public static Notification arrivalNotification(Timelog timeLog, Driver driver){

        String message = "Good day" + driver.getFirstname() + driver.getLastname() +
                "<br> Welcome to Harare Institute of Technology <br> Your entry time is:" +
                timeLog.getLoggedIn() + "<br>";

         Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setDestination(driver.getEmail());
        notification.setType("Welcome to HIT");
        notification.setMessage(message);

        return notification;
    }

    public static Notification departureNotification(Timelog timeLog, Driver driver){

            String message = "Good day" + driver.getFirstname() + driver.getLastname() +
                    "<br>We hope you have fruitful day at HIT!! <br> Your exit time was:" +
                    timeLog.getLoggedIn() + "<br>";

            Notification notification = new Notification();

            notification.setId(Util.uuid());
            notification.setCreated(Util.currentTime());
            notification.setUpdated(Util.currentTime());
            notification.setDestination(driver.getEmail());
            notification.setType("Thank you for your visit");
            notification.setMessage(message);

            return notification;


    }

    public static Notification investigateIncorrectEntry(Timelog timeLog, Vehicle vehicle){

        String message = "Good day Admin"  +
                "<br>Please investigate vehicle " + vehicle.getLicensePlate() +  " as is is attempting to " +
                "exit premises whilst its already flagged as LOGGED IN.<br>";

        Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setDestination("h170198q@hit.ac.zw");
        notification.setType("Security Alert");
        notification.setMessage(message);

        return notification;
    }

    public static Notification investigateIncorrectExit(Timelog timeLog, Vehicle vehicle){

        String message = "Good day Admin"  +
                "<br>Please investigate vehicle " + vehicle.getLicensePlate() +  " as is is attempting to " +
                "entry premises whilst its already flagged as LOGGED OUT.<br>";

        Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setDestination("h170198q@hit.ac.zw");
        notification.setType("Security Alert");
        notification.setMessage(message);

        return notification;
    }



    public static Notification blockedNotification(Timelog timeLog){

        String message = "Good day Admin" +
                "<br>A blacklisted number plate is attempting to enter the<br>Attempt entry time is:" +
                timeLog.getLoggedIn() + "<br>";

        Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setDestination("h170198q@hit.ac.zw");
        notification.setType("Security Alert!!");
        notification.setMessage(message);

        return notification;
    }


    public static Notification blockedVehicleExitNotification(Timelog timeLog){

        String message = "Good day Admin" +
                "<br>A blacklisted number plate has exited the premises<br>" +
                "Exit time is:" +
                timeLog.getLoggedIn() + "<br>";

        Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setDestination("h170198q@hit.ac.zw");
        notification.setType("Security Alert!!");
        notification.setMessage(message);

        return notification;
    }


    public static Notification registrationNotification(Vehicle vehicle){
        String message = "Good day Admin" +
                "<br> New a new vehicle with license plate" + vehicle.getLicensePlate() +
                "has been added to the database. " +
                "Please add driver details to the associated vehicle on the following URL " +
                "<br> localhost:8080/vehicles";
        Notification notification = new Notification();

        notification.setId(Util.uuid());
        notification.setCreated(Util.currentTime());
        notification.setUpdated(Util.currentTime());
        notification.setType("Driver Registration request");
        notification.setDestination("h170198q@hit.ac.zw");
        notification.setMessage(message);
        return notification;
    }
}
